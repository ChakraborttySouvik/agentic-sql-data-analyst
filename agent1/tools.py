"""
tools.py
Execute SQL queries on PostgreSQL.
"""

import logging
import os
import re

import psycopg2
from urllib.parse import urlparse

from practice.config import (
    DB_CONFIG,
    DB_STATEMENT_TIMEOUT_MS,
    DEFAULT_ROW_LIMIT,
)
from practice.sql_validator import validate_sql


logger = logging.getLogger(__name__)


def _apply_default_limit(sql: str) -> str:
    """Add a conservative LIMIT when the query does not already define one."""
    if re.search(r"\bLIMIT\b", sql, flags=re.IGNORECASE):
        return sql

    stripped = sql.strip()
    suffix = ";"

    if stripped.endswith(";"):
        stripped = stripped[:-1].strip()

    return f"{stripped} LIMIT {DEFAULT_ROW_LIMIT}{suffix}"


def execute_sql(sql):
    is_valid, message = validate_sql(sql)

    if not is_valid:
        raise ValueError(message)

    sql = _apply_default_limit(sql)
    logger.info("Executing read-only SQL")

    conn = None
    cursor = None

    try:
        database_url = os.getenv("DATABASE_URL")

        if database_url:
            url = urlparse(database_url)

            conn = psycopg2.connect(
                host=url.hostname,
                port=url.port,
                database=url.path.lstrip("/"),
                user=url.username,
                password=url.password,
                sslmode="require"
            )
        else:
            conn = psycopg2.connect(**DB_CONFIG)

        conn.set_session(readonly=True, autocommit=False)
        cursor = conn.cursor()

        cursor.execute(
            "SET LOCAL statement_timeout = %s;",
            (DB_STATEMENT_TIMEOUT_MS,)
        )

        cursor.execute(sql)

        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        rows = cursor.fetchall() if cursor.description else []

        conn.rollback()
        logger.info("SQL returned %s rows", len(rows))

        return columns, rows

    except Exception as e:
        logger.exception("Database execution failed")
        raise

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

if __name__ == "__main__":

    columns, rows = execute_sql(
        "SELECT COUNT(*) AS total_orders FROM orders;"
    )

    print("Columns:", columns)
    print("Rows:", rows)

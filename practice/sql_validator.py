"""
sql_validator.py
Validates generated SQL before execution.
"""

import re


BLOCKED_SQL_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE",
    "CREATE", "REPLACE", "MERGE", "GRANT", "REVOKE",
]


def _has_balanced_parentheses(sql: str) -> bool:
    depth = 0

    for char in sql:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                return False

    return depth == 0


def _is_single_statement(sql: str) -> bool:
    stripped = sql.strip()

    if ";" not in stripped:
        return True

    if stripped.count(";") > 1:
        return False

    return stripped.endswith(";")


def validate_sql(sql: str):

    if not sql or not sql.strip():
        return False, "SQL is empty."

    sql = sql.strip()
    sql_upper = sql.upper()

    if "--" in sql or "/*" in sql or "*/" in sql:
        return False, "SQL comments are not allowed."

    if not _is_single_statement(sql):
        return False, "Multiple SQL statements are not allowed."

    normalized = re.sub(r"\s+", " ", sql_upper).strip()
    normalized_no_semicolon = normalized[:-1].strip() if normalized.endswith(";") else normalized

    if normalized_no_semicolon.startswith("SELECT"):
        pass
    elif normalized_no_semicolon.startswith("WITH"):
        if not re.search(r"\bSELECT\b", normalized_no_semicolon):
            return False, "WITH queries must contain a SELECT statement."
    else:
        return False, "Only SELECT queries or WITH ... SELECT queries are allowed."

    for keyword in BLOCKED_SQL_KEYWORDS:
        if re.search(rf"\b{keyword}\b", normalized_no_semicolon):
            return False, f"Blocked SQL keyword detected: {keyword}."

    if not _has_balanced_parentheses(sql):
        return False, "SQL has unbalanced parentheses."

    return True, "SQL is valid."


if __name__ == "__main__":

    tests = [
        "SELECT * FROM orders;",
        "DELETE FROM orders;",
        "SELECT COUNT(*) FROM orders",
        "SELECT * FROM orders;;",
        "SELECT * FROM orders; DROP TABLE orders;",
        "SELECT * FROM orders -- comment",
    ]

    for t in tests:
        print(validate_sql(t))

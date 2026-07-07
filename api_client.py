"""
api_client.py
Streamlit frontend API client for FastAPI backend.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
REQUEST_TIMEOUT = 15


def _error_message(response, default):
    try:
        payload = response.json()
    except ValueError:
        return default

    return payload.get("detail") or payload.get("error") or default


def _request(method, path, **kwargs):
    try:
        return requests.request(
            method,
            f"{API_BASE_URL}{path}",
            timeout=REQUEST_TIMEOUT,
            **kwargs
        )
    except requests.Timeout:
        return {"error": "The API request timed out. Please try again."}
    except requests.RequestException as exc:
        return {"error": f"Could not reach the API server: {exc}"}


def login_api(username, password):
    response = _request(
        "POST",
        "/login",
        json={
            "username": username,
            "password": password
        }
    )

    if isinstance(response, dict):
        return {"success": False, "error": response["error"]}

    if response.status_code == 200:
        return response.json()

    return {
        "success": False,
        "error": _error_message(response, "Login failed")
    }


def get_dashboard_metrics():
    response = _request("GET", "/dashboard/metrics")

    if isinstance(response, dict):
        return None

    if response.status_code == 200:
        return response.json()

    return None


def get_revenue_by_category():
    response = _request("GET", "/dashboard/revenue-by-category")

    if isinstance(response, dict):
        return []

    if response.status_code == 200:
        return response.json().get("data", [])

    return []


def get_top_products():
    response = _request("GET", "/dashboard/top-products")

    if isinstance(response, dict):
        return []

    if response.status_code == 200:
        return response.json().get("data", [])

    return []


def get_orders_by_status():
    response = _request("GET", "/dashboard/orders-by-status")

    if isinstance(response, dict):
        return []

    if response.status_code == 200:
        return response.json().get("data", [])

    return []


def get_revenue_by_country():
    response = _request("GET", "/dashboard/revenue-by-country")

    if isinstance(response, dict):
        return []

    if response.status_code == 200:
        return response.json().get("data", [])

    return []


def run_query_api(username, question):
    response = _request(
        "POST",
        "/query",
        json={
            "username": username,
            "question": question
        }
    )

    if isinstance(response, dict):
        return response

    if response.status_code == 200:
        return response.json()

    return {
        "error": _error_message(response, "Query failed")
    }


def get_history_api(username):
    response = _request("GET", f"/history/{username}")

    if isinstance(response, dict):
        return []

    if response.status_code == 200:
        return response.json().get("history", [])

    return []


def clear_history_api(username):
    response = _request("DELETE", f"/history/{username}")

    if isinstance(response, dict):
        return {"success": False, "error": response["error"]}

    if response.status_code == 200:
        return response.json()

    return {
        "success": False,
        "error": _error_message(response, "Unable to clear history")
    }

"""
LeetCode GraphQL API interface module.
Handles all HTTP requests to LeetCode's GraphQL endpoint.
"""

import os
from typing import Dict, List, Any, Optional
import requests

URL = "https://leetcode.com/graphql"

class LeetCodeAPIError(Exception):
    """Base exception for LeetCode API errors."""
    pass

class AuthenticationError(LeetCodeAPIError):
    """Raised when authentication credentials are missing or invalid."""
    pass

def _get_headers_and_cookies() -> tuple[Dict[str, str], Dict[str, str]]:
    """
    Retrieve authentication credentials from environment variables and return headers and cookies.
    
    :return: A tuple of (headers_dict, cookies_dict).
    :raises AuthenticationError: If the environment variables are not set.
    """
    session = os.environ.get("LEETCODE_SESSION")
    csrf_token = os.environ.get("LEETCODE_CSRF_TOKEN")
    
    if not session or not csrf_token:
        raise AuthenticationError("LEETCODE_SESSION and/or LEETCODE_CSRF_TOKEN environment variables are not set.")
        
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-csrftoken": csrf_token
    }
    cookies = {
        "LEETCODE_SESSION": session,
        "csrftoken": csrf_token
    }
    return headers, cookies

def _query_graphql(query: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Sends a POST request to the LeetCode GraphQL API.
    
    :param query: The GraphQL query string.
    :param variables: Variables dictionary for the query.
    :return: The JSON data response.
    :raises LeetCodeAPIError: If the request fails or GraphQL returns errors.
    """
    headers, cookies = _get_headers_and_cookies()
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
        
    try:
        response = requests.post(URL, json=payload, headers=headers, cookies=cookies, timeout=15)
        if response.status_code != 200:
            raise LeetCodeAPIError(f"HTTP error {response.status_code}: {response.text}")
            
        data = response.json()
        if "errors" in data:
            raise LeetCodeAPIError(f"GraphQL Errors: {data['errors']}")
            
        return data.get("data", {})
    except requests.RequestException as e:
        raise LeetCodeAPIError(f"Network request failed: {e}")

def get_user_status() -> Dict[str, Any]:
    """
    Retrieves the current signed-in user status.
    
    :return: User status dictionary.
    :raises AuthenticationError: If user is not signed in.
    :raises LeetCodeAPIError: If API call fails.
    """
    query = """
    query {
      userStatus {
        username
        isSignedIn
      }
    }
    """
    data = _query_graphql(query)
    status = data.get("userStatus")
    if not status or not status.get("isSignedIn"):
        raise AuthenticationError("User is not signed in. Verify your LEETCODE_SESSION and LEETCODE_CSRF_TOKEN.")
    return status

def get_recent_submissions(username: str, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Fetches recent submissions for a specific user.
    
    :param username: LeetCode username.
    :param limit: Maximum number of submissions to retrieve.
    :return: A list of recent submission dictionaries.
    :raises LeetCodeAPIError: If API query fails.
    """
    query = """
    query recentSubmissionList($username: String!, $limit: Int) {
      recentSubmissionList(username: $username, limit: $limit) {
        id
        title
        titleSlug
        timestamp
        statusDisplay
        lang
      }
    }
    """
    data = _query_graphql(query, {"username": username, "limit": limit})
    return data.get("recentSubmissionList", [])

def get_question_details(title_slug: str) -> Dict[str, Any]:
    """
    Fetches details for a specific question.
    
    :param title_slug: The slug of the problem title.
    :return: A dictionary containing questionId, title, and difficulty.
    :raises LeetCodeAPIError: If API query fails.
    """
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        difficulty
        content
        topicTags {
          name
        }
      }
    }
    """
    data = _query_graphql(query, {"titleSlug": title_slug})
    return data.get("question") or {}

def get_submission_code(submission_id: int) -> str:
    """
    Fetches the source code submitted for a specific submission ID.
    
    :param submission_id: The LeetCode submission ID.
    :return: The submitted source code as a string.
    :raises LeetCodeAPIError: If the request fails or code is empty.
    """
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
      }
    }
    """
    data = _query_graphql(query, {"submissionId": submission_id})
    details = data.get("submissionDetails") or {}
    code = details.get("code")
    if not code:
        raise LeetCodeAPIError(f"No source code found for submission ID {submission_id}.")
    return code

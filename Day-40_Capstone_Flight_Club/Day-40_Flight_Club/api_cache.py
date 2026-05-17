# =============================
# api_cache.py
# =============================

"""
This file handles cached API requests done via the requests-cache library.
"""

# =============================
# Imports
# =============================

import requests_cache
from datetime import timedelta

# =============================
# Requests API calls
# =============================

def create_api_cache():
    """
    Create and return a cached session for API calls.
    The session stores responses for 1 hour to reduce redundant requests.
    """
    return requests_cache.CachedSession(expire_after=timedelta(hours=1))

# Global cached session
cached_session = create_api_cache()

def clear_api_cache(user_input):
    """
    Clear the requests cache and reset the cached session.
    This resets the global `cached_session` with a 1-hour expiration.
    """
    global cached_session
    if user_input == "y":
        cached_session.cache.clear()
        cached_session = create_api_cache()
        print(f"✅ API cache cleared and session was reset. Expiry after: {cached_session.expire_after}\n")

def check_response_cache_status(response):
    """
    Determine if a cached session response was served over cache or not.
    This relates to the requests-cache library.
    """
    if response.from_cache:
        print(f"\n"
              f"--- Served from Cache ---")
    else:
        print(f"\n"
              f"--- Not served from Cache ---")
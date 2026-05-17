# =============================
# Config.py
# =============================

"""
This file is for easy copy and pasting of the various modules and libraries used by the program.
It is not meant to imported into any module by itself.
See it as a color palette, where you pick the parts you module needs.
See PEP 8:
'Imports should usually be on separate lines and at the top of the file.'
https://www.python.org/dev/peps/pep-08/
"""

# =============================
# Environment variables
# =============================

from dotenv import load_dotenv
import os

# Load environment variables once at the start of the program.
load_dotenv()


# =============================
# Date and time
# =============================

from datetime import timedelta, datetime

# Global variable 'today' returns today's date as YYYY-MM-DD.
today = datetime.today().strftime("%Y-%m-%d")
print(f"Today is: {today}")


# =============================
# Requests API calls
# =============================

import requests_cache

def create_api_cache():
    """
    Create and return a cached session for API calls.
    The session stores responses for 1 hour to reduce redundant requests.
    """
    new_session = requests_cache.CachedSession(expire_after=timedelta(hours=1))
    return new_session

cached_session = create_api_cache()

def clear_api_cache():
    """
    Clear the requests cache and reset the cached session.

    This resets the global `cached_session` with a 1-hour expiration.
    """
    global cached_session
    cached_session.cache.clear()
    create_api_cache()
    print(f"✅ API cache cleared and session was reset: {cached_session.expire_after}")
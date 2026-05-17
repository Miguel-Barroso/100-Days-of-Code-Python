"""
This is the config.py file, and it loads the necessary environment variables and handles global imports.
This means imports and variables used by the different modules of the program are loaded once.
"""

# Loads the necessary function from the dotenv library
from dotenv import load_dotenv
# Loads the environment variables once at the start of the program
load_dotenv()

# Imports the os module for accessing environment variables
import os
# Imports the modules for handling date and time
from datetime import timedelta, datetime
# Global variable called today give's date in YYYY-MM-DD
today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
print(f"Today is {today}")

# Imports the requests module to handle API calls
import requests
# Imports a module for request caching in order to save on API calls, which are rate limited
import requests_cache

# Python stores imported modules in its own cache. These modules can force a reload
import importlib, sys

# Global cached session (12-hour expiration)
cached_session = requests_cache.CachedSession(expire_after=timedelta(hours=12))

def clear_cache():
    global cached_session
    cached_session.cache.clear()
    cached_session = requests_cache.CachedSession(expire_after=timedelta(hours=12))
    print("✅ API cache cleared and session was reset!")

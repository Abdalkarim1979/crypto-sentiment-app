import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
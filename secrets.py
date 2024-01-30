# In secrets.py

import os

PG_DATABASE = os.environ.get("PG_DATABASE")
PG_HOST = os.environ.get("PG_HOST")
PG_PASSWORD = os.environ.get("PG_PASSWORD")
PG_USER = os.environ.get("PG_USER")
PG_PORT = os.environ.get("PG_PORT")
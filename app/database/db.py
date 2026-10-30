import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Resolve path relative to this file: db.py -> database/ -> app/ -> backend/.env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# Fallback defaults with os.getenv prevent KeyErrors if variables are missing
db_user = os.getenv("DB_USER", "postgres")
db_password = os.getenv("DB_PASSWORD", "postgres")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "textmap")

DATABASE_URL = (
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

engine = create_engine(DATABASE_URL)
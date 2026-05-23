from os import environ
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)
host = environ.get("POSTGRES_HOST")
port = environ.get("POSTGRES_PORT")
user = environ.get("POSTGRES_USER")
password = environ.get("POSTGRES_PASSWORD")
database = environ.get("POSTGRES_DB")
api_key = environ.get("GOOGLE_API_KEY")
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

db = SQLDatabase.from_uri(connection_string)
from os import environ
from config import load_env_all_files

load_env_all_files()

SERVER_IP = str(environ.get("SERVER_IP"))
SERVER_PORT = int(environ.get("SERVER_PORT", "8888"))
DATABASE_URL = str(environ.get("DATABASE_URL"))

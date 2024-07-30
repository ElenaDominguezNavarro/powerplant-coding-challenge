import os
from dotenv import load_dotenv


def load_env_all_files():
    cwd = os.getcwd()
    env_folder = cwd + "/env_files"

    for file_name in os.listdir(env_folder):
        if file_name.endswith('.env'):
            env_file = os.path.join(env_folder, file_name)
            load_dotenv(env_file)



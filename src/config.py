
from environs import Env

env = Env()
env.read_env()

EMAIL = env.str("EMAIL")
PASSWORD = env.str("PASSWORD")
SESSION_FILE = env.str("SESSION_FILE")
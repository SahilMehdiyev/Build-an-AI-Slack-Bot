import pathlib 
from functools import lru_cache

from decouple import Config, RepositoryEnv
from decouple import config


THIS_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = THIS_DIR.parent
BASE_DIR_ENV = BASE_DIR / '.env'
REPO_DIR = BASE_DIR.parent
REPO_DIR_ENV = REPO_DIR / '.env'


@lru_cache
def get_config():
    if BASE_DIR_ENV.exists():
        return Config(RepositoryEnv(BASE_DIR_ENV))
    if REPO_DIR_ENV.exists():
        return Config(RepositoryEnv(REPO_DIR_ENV))
    return config

config = get_config()


 
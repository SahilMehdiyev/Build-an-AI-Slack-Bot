import pathlib 
from functools import lru_cache

from decouple import Config, Repositoryenv


THIS_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = THIS_DIR.parent
BASE_DIR_ENV = BASE_DIR / '.env'
REPO_DIR = BASE_DIR.parent
REPO_DIR_ENV = REPO_DIR / '.env'


@lru_cache
def get_config():
    if BASE_DIR_ENV.exists():
        return Config(Repositoryenv(BASE_DIR_ENV))
    return

config = get_config()


 
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

API_PREFIX = "/api"
VERSION = "0.0.1"

config = Config(".env")

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI notes aplication")
DEBUG: bool = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
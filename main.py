from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from api.errors.http_error import http_error_handler
from api.errors.http_validation_error import http422_error_handler
from api.routers.api import router as api_router
from core import config
from core import events

def get_application() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", events.create_startup_app_handler(application))
    application.add_event_handler("shutdown", events.create_shutdown_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=config.API_PREFIX)

    return application


app = get_application()
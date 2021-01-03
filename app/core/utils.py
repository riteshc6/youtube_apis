import logging

from typing import List
from typing import Tuple

from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from config import settings
from utils import update_query_results


def _setup_logger(log_config):
    """
    Setup the logger based on the config file

    Parameters
    ----------
    log_config : dict
        configuration to setup logger
    """
    logging.config.dictConfig(log_config)


def setup_application(
        title: str,
        description: str,
        sub_applications: List[Tuple],
        **kwargs) -> FastAPI:
    """
    Configures the application and returns an application instance.

    Parameters
    ----------
    title : str
        The title of the parent application
    description : str
        The description for the parent application
    sub_applications : List[Tuple]
        A list of namedtuple containing prefix and app

    Returns
    -------
    FastAPI
        A FastAPI instance ready to run
    """
    application = FastAPI(
        title=title,
        description=description,
        docs_url=None,
        redoc_url=None,
        **kwargs
    )

    # Allow cors for all origins
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # _setup_logger(settings.LOGGING)

    for app in sub_applications:
        sub_app = FastAPI(
            title=title,
            description=description,
            root_path=app.prefix
        )
        sub_app.include_router(app.router)
        application.mount(app.prefix, sub_app)
    application.add_event_handler("startup", update_query_results)
    # logger = logging.getLogger('youtube_apis')
    # logger.debug("Application Instantiated")

    return application

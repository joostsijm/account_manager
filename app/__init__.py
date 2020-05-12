"""Deep Exploration Planner"""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from rival_regions_wrapper.rival_regions_wrapper import LocalAuthentication, RemoteAuthentication


load_dotenv()

# database
ENGINE = create_engine(os.environ["DATABASE_URI"])
SESSION = sessionmaker(bind=ENGINE)

# scheduler
SCHEDULER = BackgroundScheduler(
    daemon=True,
    job_defaults={'misfire_grace_time': 300},
)
SCHEDULER.start()

# get logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
SCHEDULER_LOGGER = logging.getLogger('apscheduler')
SCHEDULER_LOGGER.setLevel(logging.DEBUG)

# create file handler
FILE_HANDLER = logging.FileHandler('output.log')
FILE_HANDLER.setLevel(logging.DEBUG)

# create console handler
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.INFO)

# create formatter and add it to the handlers
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
STREAM_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setFormatter(FORMATTER)

# add the handlers to logger
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
SCHEDULER_LOGGER.addHandler(STREAM_HANDLER)
SCHEDULER_LOGGER.addHandler(FILE_HANDLER)

USERNAME = os.environ.get('username', None)
PASSWORD = os.environ.get('password', None)
LOGIN_METHOD = os.environ.get('login_method', None)

class MissingEnvironError(Exception):
    """Error for missing environ"""

if None in (USERNAME, PASSWORD, LOGIN_METHOD):
    raise MissingEnvironError(
        'Load the following variables in your user environment:'
        'username, password, login_method'
    )

MIDDLEWARE = LocalAuthentication(USERNAME, PASSWORD, LOGIN_METHOD)
# MIDDLEWARE = RemoteAuthentication(os.environ["API_URL"], os.environ["AUTHORIZATION"])

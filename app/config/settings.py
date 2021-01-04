import logging
import os

from environs import Env

env = Env()
env.read_env()

# The base directory of the application.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Semantic versioning of the application.
VERSION = ("1", "0", "0")


# Add application specific settings here.
BASE_URL = env.str("BASEURL")
APIKEY = env.str("APIKEY")
ES_HOSTS = env.str("ES_HOSTS")
ES_INDEX = "video"

PERIOD = 30

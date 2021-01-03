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


import os
import sys

from collections import namedtuple

# Add the current application to path
# This allows import without any prefix dots.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Do not move these imports to top
from api_v1.endpoints import router as api_v1
from core.utils import setup_application
SubApp = namedtuple("SubApp", ["prefix", "router"])

# Add all the SubApp for registration
sub_applications = [
    SubApp("/api/v1", api_v1)
]

app = setup_application(
    title="youtube_apis",
    description="App to fetch and serve youtube videos",
    sub_applications=sub_applications
)

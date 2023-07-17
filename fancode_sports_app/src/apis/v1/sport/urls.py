from src.apis.routes import Routes
from src.apis.v1.sport.api import SportsResourceApi, SportMatchesResourceApi

URL_PATTERNS = [
    Routes('/sport', SportsResourceApi),
    Routes('/sport/tour/match', SportMatchesResourceApi)
]
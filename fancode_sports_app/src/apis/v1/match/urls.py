from src.apis.routes import Routes
from src.apis.v1.match.api import MatchesResourceApi

URL_PATTERNS = [
    Routes('/match', MatchesResourceApi)
]
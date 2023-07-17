from src.apis.routes import Routes
from src.apis.v1.tour.api import TourResourceApi, TourMatchesApi

URL_PATTERNS = [
    Routes('/tour', TourResourceApi),
    Routes('/tour/matches', TourMatchesApi)
]
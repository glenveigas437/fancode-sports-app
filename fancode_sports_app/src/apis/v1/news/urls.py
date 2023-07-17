from src.apis.routes import Routes
from src.apis.v1.news.api import NewsResourceApi, NewsByMatchResourceApi, NewsBySportResourceApi, NewsByTourResourceApi

URL_PATTERNS = [
    Routes('/news', NewsResourceApi),
    Routes('/match-news', NewsByMatchResourceApi),
    Routes('/sport-news', NewsBySportResourceApi),
    Routes('/tour-news', NewsByTourResourceApi)
]
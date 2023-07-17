from src.apis.base.urls import UrlConfig
from src.apis.v1.sport.urls import URL_PATTERNS as sport_urls
from src.apis.v1.match.urls import URL_PATTERNS as match_urls
from src.apis.v1.tour.urls import URL_PATTERNS as tour_urls
from src.apis.v1.news.urls import URL_PATTERNS as news_urls

NAMESPACE = '/v1'

URL_CONFIG = UrlConfig(NAMESPACE)
URL_CONFIG.register_urls(sport_urls)
URL_CONFIG.register_urls(match_urls)
URL_CONFIG.register_urls(tour_urls)
URL_CONFIG.register_urls(news_urls)

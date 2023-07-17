from src.apis.base.urls import UrlConfig
from src.apis.v1 import urls as v1urls

URL_CONFIG = UrlConfig()
URL_CONFIG.register_urls(v1urls.URL_CONFIG.urls) 
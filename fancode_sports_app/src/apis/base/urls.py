from typing import List
from src.apis.routes import Routes

class UrlConfig:

    def __init__(self, namespace=''):
        self.urls = []
        self.namespace = namespace

    def register_urls(self, list_urls: List[Routes]):
        for route in list_urls:
            route.add_namespace(self.namespace)
            self.urls.append(route)

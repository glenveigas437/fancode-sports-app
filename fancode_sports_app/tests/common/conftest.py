import unittest
from app import app as _app
from src.app import db as _db
import json

class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        with _app.app_context():
            _db.drop_all()
            _db.create_all()
            cls.client = _app.test_client()

class FancodeTestApiClient(BaseTest):
    def create_new_sport(self, payload: dict) -> tuple[dict, int]:
        create_sport = self.client.post(f'/api/v1/sport', 
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(payload))

        return json.loads(create_sport.data), create_sport.status_code
    
    def get_all_sports(self) -> tuple[dict, int]:
        all_sports = self.client.get(f'/api/v1/sport', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_sports.data), all_sports.status_code

    def create_new_tour(self, payload: dict) -> tuple[dict, int]:
        create_tour = self.client.post(f'/api/v1/tour', 
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(payload))

        return json.loads(create_tour.data), create_tour.status_code

    def get_all_tours(self) -> tuple[dict, int]:
        all_tours = self.client.get(f'/api/v1/tour', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_tours.data), all_tours.status_code

    def create_new_match(self, payload: dict) -> tuple[dict, int]:
        create_match = self.client.post(f'/api/v1/match', 
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(payload))

        return json.loads(create_match.data), create_match.status_code

    def get_all_matches(self) -> tuple[dict, int]:
        all_matches = self.client.get(f'/api/v1/match', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_matches.data), all_matches.status_code
    
    def get_all_matches_from_sport_and_tour(self) -> tuple[dict, int]:
        all_matches = self.client.get(f'/api/v1/sport/tour/match', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_matches.data), all_matches.status_code
    
    def get_matches_by_tour_name(self, params, limit=10, offset=1) -> tuple[dict, int]:
        all_matches = self.client.get(f'/api/v1/tour/matches?tour_name={params["tour_name"]}&limit={limit}&offset={offset}', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_matches.data), all_matches.status_code
    
    def create_new_news(self, payload: dict) -> tuple[dict, int]:
        create_news = self.client.post(f'/api/v1/news', 
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(payload))

        return json.loads(create_news.data), create_news.status_code
    
    def get_all_news(self) -> tuple[dict, int]:
        all_news = self.client.get(f'/api/v1/news', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(all_news.data), all_news.status_code

    def get_news_by_tags(self, params) -> tuple[dict, int]:
        if "matchId" in params:
            news = self.client.get(f'/api/v1/match-news?matchId={params["matchId"]}', 
                                        headers={'Content-Type': 'application/json'}
                                        )
        elif "tourId" in params:
            news = self.client.get(f'/api/v1/tour-news?tourId={params["tourId"]}', 
                                        headers={'Content-Type': 'application/json'}
                                        )
        
        elif "sportId" in params:
            news = self.client.get(f'/api/v1/sport-news?sportId={params["sportId"]}', 
                                        headers={'Content-Type': 'application/json'}
                                        )

        return json.loads(news.data), news.status_code



BASE_URL = "http://localhost:5000"

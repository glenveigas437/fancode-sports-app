from unittest.mock import patch
from tests.common.conftest import FancodeTestApiClient

class NewsResourceApiTest(FancodeTestApiClient):
    def test_get_all_news(self):
        sports = ["Football", "Cricket"]

        for sport in sports:
            sport_payload = {"name": sport}
            self.create_new_sport(payload=sport_payload)

        tour_payload = {"name": "Premier League", "sportId": 1, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        tour_payload = {"name": "IPL", "sportId": 2, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        match_payload = {"name": "MUN vs MCI", "tourId": 1, "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)

        match_payload = {"name": "RCB vs CSK", "tourId": 2, "format": "T20", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)
        

        news_payloads = [
            {"title": "News 1", "description": "Description 1", "sportId": 1, "tourId": 1, "matchId": 1},
            {"title": "News 2", "description": "Description 2", "sportId": 2, "tourId": 2, "matchId": 2},
        ]
        for news_payload in news_payloads:
            self.create_new_news(payload=news_payload)

        response, status_code = self.get_all_news()

        self.assertEqual(status_code, 200)
        self.assertEqual(len(response['data']), 2)  
        self.assertEqual(response['data'][0]['title'], news_payloads[0]['title'])
        self.assertEqual(response['data'][1]['description'], news_payloads[1]['description'])

    def test_create_news(self):
        sport_payload = {"name": "Football"}
        self.create_new_sport(payload=sport_payload)

        tour_payload = {"name": "Premier League", "sportId": 1, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        match_payload = {"name": "MUN vs MCI", "tourId": 1, "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)

        news_payload = {"title": "Breaking News", "description": "New news article", "sportId": 1, "tourId": 1, "matchId": 1}
        response, status_code = self.create_new_news(payload=news_payload)

        self.assertEqual(status_code, 201)
        self.assertEqual(response['data']['title'], news_payload['title'])
        self.assertEqual(response['data']['description'], news_payload['description'])

class NewsByMatchResourceApiTest(FancodeTestApiClient):
    def test_get_news_by_match(self):

        sports = ["Football", "Cricket"]

        for sport in sports:
            sport_payload = {"name": sport}
            self.create_new_sport(payload=sport_payload)

        tour_payload = {"name": "Premier League", "sportId": 1, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        tour_payload = {"name": "IPL", "sportId": 2, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        # Create a match
        match_payload = {"name": "MUN vs MCI", "tourId": 1, "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)

        match_payload = {"name": "RCB vs CSK", "tourId": 2, "format": "T20", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)
        

        news_payloads = [
            {"title": "News 1", "description": "Description 1", "sportId": 1, "tourId": 1, "matchId": 1},
            {"title": "News 2", "description": "Description 2", "sportId": 2, "tourId": 2, "matchId": 2},
        ]
        for news_payload in news_payloads:
            self.create_new_news(payload=news_payload)

        params = {"matchId": 1}
        all_news, status_code = self.get_news_by_tags(params=params)

        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_news['data']), 1)  
        self.assertEqual(all_news['data'][0]['description'], news_payloads[0]['description'])
        self.assertEqual(all_news['data'][0]['matchId'], params["matchId"])

class NewsByTourResourceApiTest(FancodeTestApiClient):
    def test_get_news_by_tour(self):
        sports = ["Football", "Cricket"]

        for sport in sports:
            sport_payload = {"name": sport}
            self.create_new_sport(payload=sport_payload)

        tour_payload = {"name": "Premier League", "sportId": 1, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        tour_payload = {"name": "IPL", "sportId": 2, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        # Create a match
        match_payload = {"name": "MUN vs MCI", "tourId": 1, "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)

        match_payload = {"name": "RCB vs CSK", "tourId": 2, "format": "T20", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)
        

        news_payloads = [
            {"title": "News 1", "description": "Description 1", "sportId": 1, "tourId": 1, "matchId": 1},
            {"title": "News 2", "description": "Description 2", "sportId": 2, "tourId": 2, "matchId": 2},
        ]
        for news_payload in news_payloads:
            self.create_new_news(payload=news_payload)
        
        params = {"tourId": 2}
        all_news, status_code = self.get_news_by_tags(params=params)

        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_news['data']), 1)  
        self.assertEqual(all_news['data'][0]['description'], news_payloads[1]['description'])
        self.assertEqual(all_news['data'][0]['tourId'], params["tourId"])

class NewsBySportResourceApiTest(FancodeTestApiClient):
    def test_get_news_by_sport(self):
        sports = ["Football", "Cricket"]

        for sport in sports:
            sport_payload = {"name": sport}
            self.create_new_sport(payload=sport_payload)

        tour_payload = {"name": "Premier League", "sportId": 1, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        tour_payload = {"name": "IPL", "sportId": 2, "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        self.create_new_tour(payload=tour_payload)

        match_payload = {"name": "MUN vs MCI", "tourId": 1, "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)

        match_payload = {"name": "RCB vs CSK", "tourId": 2, "format": "T20", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"}
        self.create_new_match(payload=match_payload)
        

        news_payloads = [
            {"title": "News 1", "description": "Description 1", "sportId": 1, "tourId": 1, "matchId": 1},
            {"title": "News 2", "description": "Description 2", "sportId": 2, "tourId": 2, "matchId": 2},
        ]
        for news_payload in news_payloads:
            self.create_new_news(payload=news_payload)

        params = {"sportId": 1}
        all_news, status_code = self.get_news_by_tags(params=params)

        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_news['data']), 1)  
        self.assertEqual(all_news['data'][0]['description'], news_payloads[0]['description'])
        self.assertEqual(all_news['data'][0]['sportId'], params["sportId"])
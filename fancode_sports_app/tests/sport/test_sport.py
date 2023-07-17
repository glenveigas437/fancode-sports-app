from unittest.mock import patch
from tests.common.conftest import FancodeTestApiClient

class SportTestResource(FancodeTestApiClient):
    def test_add_sport(self):

        sport_payload = {"name": "Football"}
        
        new_sport, status_code = self.create_new_sport(payload=sport_payload)

        new_sport = new_sport['data']

        #import pdb; pdb.set_trace()
        self.assertEqual(status_code, 201)
        self.assertEqual(new_sport['name'], sport_payload['name'])
        self.assertEqual(new_sport['status'], True)

    def test_get_all_sports(self):
        
        sports = ["Cricket", "Football", "Tennis"]

        for sport in sports:
            self.create_new_sport(payload={"name": sport})
        
        all_sports, status_code = self.get_all_sports()

        all_sports = all_sports['data']
        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_sports), len(sports))
        self.assertEqual(all_sports[-1]['name'], "Tennis")


class SportMatchesTestResource(FancodeTestApiClient):
    def test_get_all_matches(self):
        sport_payloads = [
            {"name": "Cricket"},
            {"name": "Football"}
        ]
        sports = []
        for sport_payload in sport_payloads:
            sport, _ = self.create_new_sport(payload=sport_payload)
            sports.append(sport)

        
        tour_payloads = [
            {"name": "IPL", "sportId": sports[0]['data']['id'], "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"},
            {"name": "Premier League", "sportId": sports[1]['data']['id'], "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        ]
        match_payloads = [
            {"name": "CSK vs MI", "tourId": 1, "format": "T20", "startTime": "2023-07-16 20:53:10", "endTime": "2023-07-16 23:53:10"},
            {"name": "PBKS vs MI", "tourId": 1, "format": "T20", "startTime": "2023-07-19 20:53:10", "endTime": "2023-07-19 23:53:10"},
            {"name": "Arsenal vs Manchester United", "tourId": 2, "format": "Football", "startTime": "2023-07-20 20:53:10", "endTime": "2023-07-20 23:53:10"},
            {"name": "Chelsea vs Liverpool", "tourId": 2, "format": "Football", "startTime": "2023-07-23 20:53:10", "endTime": "2023-07-23 23:53:10"}
        ]
        for tour_payload in tour_payloads:
            tour, _ = self.create_new_tour(payload=tour_payload)
        for match_payload in match_payloads:
            self.create_new_match(payload=match_payload)

        all_matches, status_code = self.get_all_matches_from_sport_and_tour()
        all_matches = all_matches['data']
        
        self.assertEqual(status_code, 200)
        self.assertEqual(len(list(all_matches.keys())), len(sport_payloads))
        self.assertIn(sport_payloads[0]['name'], list(all_matches.keys()))
        
from unittest.mock import patch
from tests.common.conftest import FancodeTestApiClient

class MatchTestResource(FancodeTestApiClient):
    def test_add_match(self):

        sport_payload = {
                    "name": "Cricket"
                    }

        tour_payload = {
                    "name": "IPL",
                    "sportId": 1,
                    "startTime": "2023-07-16 08:22:52",
                    "endTime": "2023-08-16 08:22:52"
                    }
        
        match_payload = {
                "name": "CSK vs MI",
                "tourId": 1,
                "format": "T20",
                "startTime": "2023-07-16 20:53:10",
                "endTime": "2023-07-16 23:53:10"
                }
        
        created_sport, status_code = self.create_new_sport(payload=sport_payload)
        new_tour, status_code = self.create_new_tour(payload=tour_payload)
        new_match, status_code = self.create_new_match(payload=match_payload)

        new_match = new_match['data']
        self.assertEqual(status_code, 201)
        self.assertEqual(new_match['name'], match_payload['name'])
        self.assertEqual(new_match['status'], True)
        self.assertEqual(new_match['format'], match_payload['format'])

    def test_get_all_matches(self):
        
        sport_payload = {
                    "name": "Cricket"
                    }
        
        created_sport, status_code = self.create_new_sport(payload=sport_payload)

        tour_payload = {
                    "name": "IPL",
                    "sportId": 1,
                    "startTime": "2023-07-16 08:22:52",
                    "endTime": "2023-08-16 08:22:52"
                }
        
        self.create_new_tour(payload=tour_payload)
        
        matches = [{
                "name": "CSK vs MI",
                "tourId": 1,
                "format": "T20",
                "startTime": "2023-07-16 20:53:10",
                "endTime": "2023-07-16 23:53:10"
                },
                {
                "name": "PBKS vs MI",
                "tourId": 1,
                "format": "T20",
                "startTime": "2023-07-19 20:53:10",
                "endTime": "2023-07-19 23:53:10"
                },
                ]
        
        for match in matches:
            self.create_new_match(payload=match)
        
        all_matches, status_code = self.get_all_matches()

        all_matches = all_matches['data']
        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_matches), len(matches))
        self.assertEqual(all_matches[-1]['tourId'], created_sport['data']['id'])
        self.assertEqual(all_matches[0]['format'], matches[0]['format'])

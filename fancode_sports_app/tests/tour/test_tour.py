from unittest.mock import patch
from tests.common.conftest import FancodeTestApiClient

class TourTestResource(FancodeTestApiClient):
    def test_add_tour(self):

        sport_payload = {
                    "name": "Cricket"
                    }

        tour_payload = {
                    "name": "IPL",
                    "sportId": 1,
                    "startTime": "2023-07-16 08:22:52",
                    "endTime": "2023-08-16 08:22:52"
                    }
        
        created_sport, status_code = self.create_new_sport(payload=sport_payload)
        new_tour, status_code = self.create_new_tour(payload=tour_payload)

        new_tour = new_tour['data']
        self.assertEqual(status_code, 201)
        self.assertEqual(new_tour['name'], tour_payload['name'])
        self.assertEqual(new_tour['status'], True)
        self.assertEqual(new_tour['sportId'], created_sport['data']['id'])

    def test_get_all_tours(self):
        
        sport_payload = {
                    "name": "Cricket"
                    }
        
        created_sport, status_code = self.create_new_sport(payload=sport_payload)

        tours = [{
                    "name": "IPL",
                    "sportId": 1,
                    "startTime": "2023-07-16 08:22:52",
                    "endTime": "2023-08-16 08:22:52"
                },
                 {
                    "name": "ICC Cricket WC",
                    "sportId": 1,
                    "startTime": "2023-07-16 08:22:52",
                    "endTime": "2023-08-16 08:22:52"
                    }]
        
        for tour in tours:
            self.create_new_tour(payload=tour)
        
        all_tours, status_code = self.get_all_tours()

        all_tours = all_tours['data']
        self.assertEqual(status_code, 200)
        self.assertEqual(len(all_tours), len(tours))
        self.assertEqual(all_tours[-1]['sportId'], 1)


class TourMatchesTestResource(FancodeTestApiClient):
    def test_get_matches_by_tour_name(self):
        sport_payloads = [
            {"name": "Cricket"},
            {"name": "Football"},
            {"name": "Tennis"}
        ]
        sports = []
        for sport_payload in sport_payloads:
            sport, _ = self.create_new_sport(payload=sport_payload)
            sports.append(sport)

        tour_payloads = [
            {"name": "IPL", "sportId": sports[0]['data']['id'], "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"},
            {"name": "Premier League", "sportId": sports[1]['data']['id'], "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"},
            {"name": "Wimbledon", "sportId": sports[2]['data']['id'], "startTime": "2023-07-16 08:22:52", "endTime": "2023-08-16 08:22:52"}
        ]
        tours = []
        for tour_payload in tour_payloads:
            tour, _ = self.create_new_tour(payload=tour_payload)
            tours.append(tour)

        match_payloads = [
            {"name": "CSK vs MI", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-16 20:53:10", "endTime": "2023-07-16 23:53:10"},
            {"name": "PBKS vs MI", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-19 20:53:10", "endTime": "2023-07-19 23:53:10"},
            {"name": "RR vs SRH", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-21 20:53:10", "endTime": "2023-07-21 23:53:10"},
            {"name": "PBKS vs CSK", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-16 20:53:10", "endTime": "2023-07-16 23:53:10"},
            {"name": "RR vs MI", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-19 20:53:10", "endTime": "2023-07-19 23:53:10"},
            {"name": "CSK vs SRH", "tourId": tours[0]['data']['id'], "format": "T20", "startTime": "2023-07-21 20:53:10", "endTime": "2023-07-21 23:53:10"},
            {"name": "MUN vs MCI", "tourId": tours[1]['data']['id'], "format": "Football", "startTime": "2023-07-18 18:00:00", "endTime": "2023-07-18 20:00:00"},
            {"name": "ARS vs TOT", "tourId": tours[1]['data']['id'], "format": "Football", "startTime": "2023-07-20 18:00:00", "endTime": "2023-07-20 20:00:00"},
            {"name": "FED vs DJO", "tourId": tours[2]['data']['id'], "format": "Singles", "startTime": "2023-07-19 14:00:00", "endTime": "2023-07-19 17:00:00"}
        ]
        matches = []
        for match_payload in match_payloads:
            match, _ = self.create_new_match(payload=match_payload)
            matches.append(match)

        params = {"tour_name": "IPL", "sport": "Cricket"}
        response, status_code = self.get_matches_by_tour_name(params=params)
        matches_by_tour = response['data']

        
        self.assertEqual(status_code, 200)
        self.assertEqual(len(matches_by_tour), 6)  
        self.assertEqual(matches_by_tour[0]['sport'],params["sport"])
        
        limit = 2
        offset = 3

        response, status_code = self.get_matches_by_tour_name(params=params, limit=limit, offset=offset)
        matches_by_tour = response['data']

        self.assertEqual(len(matches_by_tour), limit)

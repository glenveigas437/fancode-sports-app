from flask import request
from src.app import api, db
from src.apis.base.api import BaseApi 
from src.apis.base.utils import pagination
from src.apis.v1.sport.dto import sport_create_model
from src.apis.v1.sport.orm_queries import get_all_sports_tour_and_matches

class SportsResourceApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'limit': {
            'type': 'int',
            'default': '10'
        },
        'offset': {
            'type': 'int',
            'default': '1'
        }
    })
    def get(self):
        from .models import Sport
        query = db.session.query(Sport)
        sports, paginate = pagination(schema=query)

        all_sports = []
        for sport in sports:
            sport = sport.serialize()
            all_sports.append(sport)

        
        return self.build_response(data=all_sports, pagination=paginate)
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'})
    @api.response(201, 'Created')
    @api.expect(sport_create_model)
    def post(self):
        from .models import Sport
        data = request.json
        name = data['name']

        sport = Sport(name=name)
        
        try:
            with db.session.begin():
                db.session.add(sport)
                db.session.commit()

            serialized_sport = sport.serialize()
            return self.build_single_response(data=serialized_sport)
        except Exception as e:
            error_message = str(e)
            return self.build_errors(data=error_message)


class SportMatchesResourceApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'limit': {
            'type': 'int',
            'default': '10'
        },
        'offset': {
            'type': 'int',
            'default': '1'
        }
    })
    def get(self):
        all_matches_query = get_all_sports_tour_and_matches()
        all_matches, paginate = pagination(schema=all_matches_query)

        all_matches_dict = {}
        for match in all_matches:
            match_data = match[0].match_serialize()
            if match[1] not in all_matches_dict:
                all_matches_dict[match[1]]={}
            if match[2] not in all_matches_dict[match[1]]:
                all_matches_dict[match[1]][match[2]] = []
            all_matches_dict[match[1]][match[2]].append(match_data)
    
        return self.build_response(data=all_matches_dict, pagination=paginate)
    
    

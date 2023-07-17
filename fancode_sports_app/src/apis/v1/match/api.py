from flask import request
from src.app import api, db
from src.apis.base.api import BaseApi 
from src.apis.base.utils import pagination
from src.apis.v1.match.dto import match_create_model

class MatchesResourceApi(BaseApi):
    
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
        from .models import Match
        query = db.session.query(Match)
        matches, paginate = pagination(schema=query)

        all_matches = []
        for match in matches:
            match = match.serialize()
            all_matches.append(match)
        
        return self.build_response(data=all_matches, pagination=paginate)
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'})
    @api.response(201, 'Created')
    @api.expect(match_create_model)
    def post(self):
        from .models import Match
        data = request.json
        name = data['name']
        tourId = data['tourId']
        match_format = data['format']
        startTime = data['startTime']
        endTime = data['endTime']

        match = Match(name=name, tourId=tourId, format=match_format, startTime=startTime, endTime=endTime)
        
        try:
            with db.session.begin():
                db.session.add(match)
                db.session.commit()

            serialized_match = match.serialize()
            return self.build_single_response(data=serialized_match)
        except Exception as e:
            error_message = str(e)
            return self.build_errors(data=error_message)
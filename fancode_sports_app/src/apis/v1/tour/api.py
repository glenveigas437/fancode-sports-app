from flask import request
from src.app import api, db
from src.apis.base.api import BaseApi 
from src.apis.base.utils import pagination
from src.apis.v1.tour.dto import tour_create_model
from src.apis.v1.match.models import Match

class TourResourceApi(BaseApi):
    
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
        from .models import Tour
        query = db.session.query(Tour)
        tours, paginate = pagination(schema=query)

        all_tours = []
        for tour in tours:
            tour = tour.serialize()
            all_tours.append(tour)

        
        return self.build_response(data=all_tours, pagination=paginate)
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'})
    @api.response(201, 'Created')
    @api.expect(tour_create_model)
    def post(self):
        from .models import Tour
        data = request.json

        #import pdb; pdb.set_trace()
        name = data['name']
        sport_id = data['sportId'],
        start_time = data['startTime'],
        end_time = data['endTime']

        tour = Tour(name=name, sportId=sport_id, startTime=start_time, endTime=end_time)
        
        try:
            with db.session.begin():
                db.session.add(tour)
                db.session.commit()

            serialized_tour = tour.serialize()
            return self.build_single_response(data=serialized_tour)
        except Exception as e:
            error_message = str(e)
            return self.build_errors(data=error_message)


class TourMatchesApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'tour_name': {
            'type': 'string',
            'description': 'Tour name',
            'required': True
        },
        'limit': {
            'type': 'integer',
            'default': 10,
            'description': 'Number of matches to retrieve'
        },
        'offset': {
            'type': 'integer',
            'default': 0,
            'description': 'Offset for pagination'
        }
    })
    def get(self):
        from .models import Tour
        tour_name = request.args.get('tour_name')
        limit = request.args.get('limit', default=10, type=int)
        offset = request.args.get('offset', default=0, type=int)
        
        if not tour_name:
            return self.build_errors(message='Tour name is required', status_code=400)
        
        tour = Tour.query.filter_by(name=tour_name).first()
        
        if not tour:
            return self.build_errors(data='Tour not found', status_code=404)
        
        query = Match.query.filter_by(tourId=tour.id)
        matches, paginate = pagination(schema=query)
        serialized_matches = [match.match_detail_serialize() for match in matches]
        
        return self.build_response(data=serialized_matches, pagination=paginate)

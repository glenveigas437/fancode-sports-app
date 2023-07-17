from flask import request
from src.app import api, db
from src.apis.base.api import BaseApi 
from src.apis.base.utils import pagination
from src.apis.v1.news.dto import news_create_model

class NewsResourceApi(BaseApi):
    
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
        from .models import News
        query = db.session.query(News)
        news_obj, paginate = pagination(schema=query)

        all_news = []
        for news in news_obj:
            news = news.serialize()
            all_news.append(news)
        
        return self.build_response(data=all_news, pagination=paginate)
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'})
    @api.response(201, 'Created')
    @api.expect(news_create_model)
    def post(self):
        from .models import News
        data = request.json

        title = data['title']
        description = data['description']
        sportId = data['sportId']
        tourId = data['tourId']
        matchId = data['matchId']

        news = News(title=title, tourId=tourId, description=description, sportId=sportId, matchId=matchId)
        
        try:
            with db.session.begin():
                db.session.add(news)
                db.session.commit()

            serialized_match = news.serialize()
            return self.build_single_response(data=serialized_match)
        except Exception as e:
            error_message = str(e)
            return self.build_errors(data=error_message)

class NewsByMatchResourceApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'matchId': {
            'type': 'int',
            'description': 'Match ID'
        },
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
        from .models import News
        match_id = request.args.get('matchId')
        query = db.session.query(News).filter_by(matchId=match_id)
        news_obj, paginate = pagination(schema=query)

        all_news = []
        for news in news_obj:
            news = news.serialize()
            all_news.append(news)
        
        return self.build_response(data=all_news, pagination=paginate)

class NewsByTourResourceApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'tourId': {
            'type': 'int',
            'description': 'Tour ID'
        },
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
        from .models import News
        tour_id = request.args.get('tourId')
        query = db.session.query(News).filter_by(tourId=tour_id)
        news_obj, paginate = pagination(schema=query)

        all_news = []
        for news in news_obj:
            news = news.serialize()
            all_news.append(news)
        
        return self.build_response(data=all_news, pagination=paginate)

class NewsBySportResourceApi(BaseApi):
    
    @api.doc(responses={400: 'Bad Request', 404: 'Not Found'}, params={
        'sportId': {
            'type': 'int',
            'description': 'Sport ID'
        },
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
        from .models import News
        sport_id = request.args.get('sportId')
        query = db.session.query(News).filter_by(sportId=sport_id)
        news_obj, paginate = pagination(schema=query)

        all_news = []
        for news in news_obj:
            news = news.serialize()
            all_news.append(news)
        
        return self.build_response(data=all_news, pagination=paginate)

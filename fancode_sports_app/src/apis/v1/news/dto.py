from flask_restx import fields

from src.app import api

news_create_model = api.model('Create News', {
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'sportId': fields.Integer(required=True),
    'tourId': fields.Integer(required=True),
    'matchId': fields.Integer(required=True),
})
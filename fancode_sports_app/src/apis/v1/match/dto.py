from flask_restx import fields

from src.app import api

match_create_model = api.model('Create Match', {
    'name': fields.String(required=True),
    'tourId': fields.Integer(required=True),
    'format': fields.String(required=True),
    'startTime': fields.DateTime(required=True),
    'endTime': fields.DateTime(required=True)
})
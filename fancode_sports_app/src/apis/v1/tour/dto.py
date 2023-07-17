from flask_restx import fields

from src.app import api

tour_create_model = api.model('Create Tour', {
    'name' : fields.String(required=True),
    'sportId': fields.Integer(required=True),
    'startTime' : fields.DateTime(required=True),
    'endTime' : fields.DateTime(required=True)
}
)
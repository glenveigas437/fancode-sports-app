from flask_restx import fields

from src.app import api

sport_create_model = api.model('Create Sport', {
    'name' : fields.String
}
)
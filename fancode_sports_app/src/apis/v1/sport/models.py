from src.app import db
from src.apis.base.utils import convert_datetime_to_string

class Sport(db.Model):
    __tablename__ = 'sport'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    recUpdatedAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    createdAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'recUpdatedAt': convert_datetime_to_string(self.recUpdatedAt),
            'createdAt': convert_datetime_to_string(self.createdAt)
        }
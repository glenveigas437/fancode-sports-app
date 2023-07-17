from src.app import db
from src.apis.base.utils import convert_datetime_to_string

class Tour(db.Model):
    __tablename__ = 'tour'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    sportId = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    startTime = db.Column(db.TIMESTAMP, nullable=False)
    endTime = db.Column(db.TIMESTAMP, nullable=False)
    recUpdatedAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    createdAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'sportId': self.sportId,
            'status': self.status,
            'startTime': convert_datetime_to_string(self.startTime),
            'endTime': convert_datetime_to_string(self.endTime),
            'recUpdatedAt': convert_datetime_to_string(self.recUpdatedAt),
            'createdAt': convert_datetime_to_string(self.createdAt),
        }
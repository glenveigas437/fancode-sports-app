from src.app import db
from src.apis.base.utils import convert_datetime_to_string

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    tourId = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    format = db.Column(db.String(50), nullable=False)
    startTime = db.Column(db.TIMESTAMP, nullable=False)
    endTime = db.Column(db.TIMESTAMP, nullable=False)
    recUpdatedAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    createdAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'tourId': self.tourId,
            'status': self.status,
            'format': self.format,
            'startTime': convert_datetime_to_string(self.startTime),
            'endTime': convert_datetime_to_string(self.endTime),
            'recUpdatedAt': convert_datetime_to_string(self.recUpdatedAt),
            'createdAt': convert_datetime_to_string(self.createdAt),
        }

    def match_detail_serialize(self):
        from src.apis.v1.tour.models import Tour
        from src.apis.v1.sport.models import Sport

        sport_name = db.session.query(Sport.name).join(Tour, Tour.sportId==Sport.id).join(Match, self.tourId==Tour.id).first()[0]

        return {
            'name': self.name,
            'status': self.status,
            'sport': sport_name,
            'format': self.format,
            'startTime': convert_datetime_to_string(self.startTime),
            'endTime': convert_datetime_to_string(self.endTime),
        }
    
    def match_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'startTime': convert_datetime_to_string(self.startTime),
            'format': self.format
        }

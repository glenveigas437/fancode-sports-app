from src.app import db
from src.apis.base.utils import convert_datetime_to_string

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    sportId = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    tourId =  db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    matchId = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    createdAt = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'sportId': self.sportId,
            'tourId': self.tourId,
            'matchId': self.matchId,
            'createdAt': convert_datetime_to_string(self.createdAt)
        }

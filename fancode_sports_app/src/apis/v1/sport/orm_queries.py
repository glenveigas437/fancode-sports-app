from src.apis.v1.sport.models import Sport
from src.apis.v1.match.models import Match
from src.apis.v1.tour.models import Tour
from src.app import db

def get_all_sports_tour_and_matches():
    query = db.session.query(Match, Sport.name.label('Sport_name'), Tour.name.label('Tour_name'))\
           .join(Tour, Sport.id == Tour.sportId)\
           .join(Match, Match.tourId == Tour.id)
    
    return query

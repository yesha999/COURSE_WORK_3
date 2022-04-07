from application.dao.models.base import BaseModel
from application.database import db


class Favorite(BaseModel):
    __tablename__ = 'favorite'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    movie = db.relationship("Movie")

from application.dao.models.base import BaseModel
from application.database import db

class Movie(BaseModel):
    __tablename__ = 'movie'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    trailer = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director")







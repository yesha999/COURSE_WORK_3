from application.dao.models.base import BaseModel
from application.database import db


class User(BaseModel):
    __tablename__ = 'user'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String(255))  # наверное, правильнее было бы через genre_id

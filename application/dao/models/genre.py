from application.dao.models.base import BaseModel
from application.database import db


class Genre(BaseModel):
    __tablename__ = 'genre'
    name = db.Column(db.String(255), nullable=False, unique=True)

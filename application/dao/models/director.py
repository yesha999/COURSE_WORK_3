from application.dao.models.base import BaseModel
from application.database import db


class Director(BaseModel):
    __tablename__ = 'director'
    name = db.Column(db.String(255), nullable=False, unique=True)

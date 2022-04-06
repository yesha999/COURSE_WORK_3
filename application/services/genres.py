from application.dao.genres import GenresDAO
from application.services.helpers.schemas.genre import GenreSchema



class GenresService:

    def __init__(self, dao: GenresDAO, schema: GenreSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        return self.schema.dump(self.dao.get_one(uid))

from application.dao.directors import DirectorsDAO
from application.services.helpers.schemas.director import DirectorSchema


class DirectorsService:

    def __init__(self, dao: DirectorsDAO, schema: DirectorSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        return self.schema.dump(self.dao.get_one(uid))

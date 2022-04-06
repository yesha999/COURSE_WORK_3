from application.dao.movies import MoviesDAO
from application.services.helpers.schemas.movie import MovieSchema


class MoviesService:

    def __init__(self, dao: MoviesDAO, schema: MovieSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        """Сериализуем все фильмы"""
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        """Сериализуем 1 фильм"""
        return self.schema.dump(self.dao.get_one(uid))

    def get_by_filters(self, filters):
        limit = 0
        offset = 0
        if filters.get('page'):
            try:
                page = int(filters.get('page'))
                limit = 12
                offset = (page-1) * limit
            except TypeError:
                pass

        return self.schema.dump(self.dao.get_by_filters(filters, limit, offset), many=True)

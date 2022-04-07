from application.dao.favorites import FavoritesDAO
from application.services.helpers.schemas.favorite import FavoriteSchema

class FavoritesService:

    def __init__(self, dao: FavoritesDAO, schema: FavoriteSchema):
        self.dao = dao
        self.schema = schema

    def add_favorite(self, user_id: int, movie_id: int):
        return self.schema.dump(self.dao.add_favorite(user_id, movie_id))

    def del_favorite(self, user_id: int, movie_id: int):
        return self.schema.dump(self.dao.del_favorite(user_id, movie_id))

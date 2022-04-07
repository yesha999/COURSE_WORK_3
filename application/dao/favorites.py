from application.dao.models.favorite import Favorite


class FavoritesDAO:
    def __init__(self, session):
        self.session = session

    def add_favorite(self, user_id, movie_id):
        """Добавляем новую закладку, получаем его же"""
        data = {'user_id': user_id, 'movie_id': movie_id}
        new_favorite = Favorite(**data)
        self.session.add(new_favorite)
        self.session.commit()

        return new_favorite

    def del_favorite(self, user_id, movie_id):
        """Удаляем закладку, получаем его же"""
        deleted_favorite = self.session.query(Favorite).filter(Favorite.user_id == user_id,
                                                               Favorite.movie_id == movie_id).first()
        if deleted_favorite:
            self.session.delete(deleted_favorite)
            self.session.commit()
            return ''
        else:
            return 'Закладка не найдена :('

from sqlalchemy import desc, asc

from application.dao.models.movie import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получаем все фильмы (несериализованные)"""
        return self.session.query(Movie).all()

    def get_one(self, uid: int):
        """Получаем 1 фильм (несериализованный)"""
        return self.session.query(Movie).get(uid)

    def get_by_filters(self, filters: dict, limit: int, offset: int):
        movies = self.session.query(Movie)

        if 'director_id' in filters:
            movies = movies.filter(Movie.director_id == filters['director_id'])

        if 'genre_id' in filters:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])

        if 'year' in filters:
            movies = movies.filter(Movie.year == filters['year'])

        if 'status' in filters:
            if filters['status'] == 'new':
                movies = movies.order_by(desc(Movie.year))
            if filters['status'] == 'old':
                movies = movies.order_by(asc(Movie.year))

        if limit > 0:
            movies = movies.limit(limit).offset(offset)

        return movies

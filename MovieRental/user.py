from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return F"User: {self.name}"

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self, name):
        movie_list = list(filter(lambda x: x.name != name, self.movies))
        self.movies = movie_list

    def watched_movies(self):
        movies = list(filter(lambda x: x.watched, self.movies))
        return movies

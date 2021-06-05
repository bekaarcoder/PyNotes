from movie import Movie
import json


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

    def save_to_file(self):
        with open(f"{self.name}.txt", 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(f"{movie.name}, {movie.genre}, {str(movie.watched)}\n")

    @classmethod
    def load_from_file(cls, filename):
        with open(f"{filename}.txt", 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")
                movies.append(Movie(movie_data[0].strip(), movie_data[1].strip(), movie_data[2].strip() == "True"))

            user = cls(username)
            user.movies = movies
            return user

    def save_as_json(self):
        data = {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

        with open(f"{self.name}.json", 'w') as f:
            json.dump(data, f)

        return data

    @classmethod
    def load_from_json(cls, filename):
        with open(f"{filename}.json", 'r') as f:
            json_data = json.load(f)
            username = json_data['name']
            movies = []
            for movie in json_data['movies']:
                movies.append(Movie.from_json(movie))

            user = cls(username)
            user.movies = movies
            return user

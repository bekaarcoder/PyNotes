from user import User

user = User("Rahul")

user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("Harry Potter", "Fantasy")

print(user)
print(user.movies)
print(user.watched_movies())

user.delete_movie("Harry Potter")
print(user.movies)
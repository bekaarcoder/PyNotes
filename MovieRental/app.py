from user import User
import json

user = User("Rahul")

# user.add_movie("The Matrix", "Sci-Fi")
# user.add_movie("Harry Potter", "Fantasy")
#
# print(user.save_as_json())

load_data = User.load_from_json(user.name)
print(load_data.movies)
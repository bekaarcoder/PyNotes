from user import User
from database import Database

Database.initialize(
    user="postgres", password="postgres", database="learning", host="localhost"
)

# new_user = User("janesmith@gmail.com", "Jane", "Smith", None)

# new_user.save_to_db()

# my_user = User.load_from_db_by_email("rahulsharma@gmail.com")
# print(my_user.first_name)

User.delete_user_by_email("rahulsharma@gmail.com")
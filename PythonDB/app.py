from user import User

# new_user = User("bruce@gmail.com", "Anne", "Smith", None)

# new_user.save_to_db()

my_user = User.load_from_db_by_email("rahulsharma@gmail.com")
print(my_user.first_name)

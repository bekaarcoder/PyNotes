from database import ConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"User: {self.email}"

    def save_to_db(self):
        with ConnectionFromPool() as cursor:
            cursor.execute(
                "insert into users (email, first_name, last_name) values (%s, %s, %s)",
                (self.email, self.first_name, self.last_name),
            )

    @classmethod
    def delete_user_by_email(cls, email):
        with ConnectionFromPool() as cursor:
            cursor.execute("delete from users where email = %s", (email,))

    @classmethod
    def load_from_db_by_email(cls, email):
        with ConnectionFromPool() as cursor:
            cursor.execute("select * from users where email = %s", (email,))
            user_data = cursor.fetchone()
            return cls(
                email=user_data[1],
                first_name=user_data[2],
                last_name=user_data[3],
                id=user_data[0],
            )

import db_base as db


class User:
    def __init__(self, row):
        self.userid = row[0]
        self.user_name = row[1]
        self.role = row[2]


class UserDB(db.DBbase):
    def reset_or_create_db(self):
        sql = """
        DROP TABLE IF EXISTS Users;

        CREATE TABLE Users (
            userid INTEGER NOT NULL PRIMARY KEY UNIQUE,
            user_name TEXT,
            role TEXT
        );
        """

        super().execute_script(sql)

    def read_user_data(self):
        self.user_list = [
            [1, "admin_user", "manager"],
            [2, "user_1", "user"]
        ]

    def save_to_db(self):
        for row in self.user_list:
            user = User(row)
            try:
                super().get_cursor.execute("""

                INSERT INTO Users (
                    userid,
                    user_name,
                    role
                )
                VALUES(?,?,?)

                """, (user.userid, user.user_name, user.role))

                super().get_connection.commit()
                print("Saved to DB:", user.userid, user.user_name)

            except Exception as e:
                print(e)
                print("Save to DB aborted")


user_db = UserDB("RecipeDB.sqlite")
user_db.reset_or_create_db()
user_db.read_user_data()
user_db.save_to_db()

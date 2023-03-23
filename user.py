import db_base as db
import recipe


class User:
    def __init__(self, row):
        self.userid = row[0]
        self.user_name = row[1]
        self.role = row[2]


class UserDB(recipe.RecipeDB):
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
            [1, "admin_user", "admin"],
            [2, "user_1", "user"]
        ]

    def save_to_db(self):
        for row in self.user_list:
            user = User(row)
            try:
                super().get_cursor.execute("""

                INSERT OR IGNORE INTO Users (
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

    def add_user(self, userid, user_name, role):
        try:
            super().get_cursor.execute("""

                INSERT OR IGNORE INTO Users (
                    userid,
                    user_name,
                    role
                )
                VALUES(?,?,?)

                """, (userid, user_name, role))

            super().get_connection.commit()
            print(f"Added {user_name} successfully.")
        except Exception as e:
            print("An error has occurred.", e)

    def delete_user(self, userid):
        try:
            super().get_cursor.execute("DELETE FROM Users WHERE userid=?", (userid,))
            super().get_connection.commit()
            print(f"Record with userid {userid} deleted successfully.")
        except Exception as e:
            print(e)
            print(f"Failed to delete record with id {userid}.")


    def get_user_role_by_name(self, user_name):
        try:
            super().get_cursor.execute("SELECT role FROM Users WHERE user_name=?", (user_name,))
            role = super().get_cursor.fetchone()[0]
            if role !="":
                return role
            else:
                print(f"No record found with user_name {user_name}.")
        except Exception as e:
            print(e)
            print(f"Failed to get record with user_name {user_name}.")


    def get_user_name_by_name(self, user_name):
        try:
            super().get_cursor.execute("SELECT user_name FROM Users WHERE user_name=?", (user_name,))
            user_name = super().get_cursor.fetchone()[0]
            if user_name !="":
                return user_name
            else:
                print(f"No record found with user_name {user_name}.")
        except Exception as e:
            print(e)
            print(f"Failed to get record with user_name {user_name}.")
            return ''

user_db = UserDB("RecipeDB.sqlite")
# user_db.reset_or_create_db()
# user_db.read_user_data()
# user_db.save_to_db()
# user_db.add_user(3, 'user_2', 'user')
# user_db.delete_user(3)
# user_db.get_user_role_by_name('user_1')
user_db.get_user_name_by_name('user_2')

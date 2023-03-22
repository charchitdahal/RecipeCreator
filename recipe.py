import db_base as db
import csv


class Recipe:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.category = row[2]


class RecipeDB(db.DBbase):
    def reset_or_create_db(self):
        sql = """
        DROP TABLE IF EXISTS Recipe;
        
        CREATE TABLE Recipe (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            name TEXT,
            category varchar(20) NOT NULL
        );
        """

        super().execute_script(sql)
        try:
            pass
        except Exception as e:
            print(e)

    def read_recipe_data(self, file_name):
        self.recipe_list = []

        try:
            with open(file_name, "r") as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    recipe = Recipe(row)
                    self.recipe_list.append(recipe)
        except Exception as e:
            print(e)

    def save_to_db(self):
        print("Number of recipes saved:", len(self.recipe_list))
        save = input("Do you want to save the recipes to the database? (y/n)").lower()
        if save == "y":
            for item in self.recipe_list:
                try:
                    super().get_cursor.execute("""
                    
                    INSERT OR IGNORE INTO Recipe (
                        id,
                        name ,
                        category
                    )
                    VALUES(?,?,?)
                    
                    """, (item.id, item.name, item.category))

                    super().get_connection.commit()
                    print("Saved to DB:", item.id, item.name)

                except Exception as e:
                    print(e)
                    print("Save to DB aborted")

    def add_recipe(self, id, name, category):
        try:
            super().get_cursor.execute("""

            INSERT OR IGNORE INTO Recipe (
                id,
                name ,
                category  
            )
            VALUES(?,?,?)

            """, (id, name, category))
            super().get_connection.commit()
            print(f"Added {name} successfully.")
        except Exception as e:
            print("An error has occurred.", e)

    def delete_recipe(self, id):
        try:
            super().get_cursor.execute("DELETE FROM Recipe WHERE id=?", (id,))
            super().get_connection.commit()
            print(f"Record with id {id} deleted successfully.")
        except Exception as e:
            print(e)
            print(f"Failed to delete record with id {id}.")

# recipe_db = RecipeDB("RecipeDB.sqlite")
# recipe_db.reset_or_create_db()
# recipe_db.read_recipe_data("recipes.csv")
# recipe_db.save_to_db()
# recipe_db.add_recipe(21, 'Butter Chicken', 'Indian')
# recipe_db.delete_recipe(21)

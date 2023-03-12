import db_base as db
import csv

class Recipe:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.category = row[2]
        self.ingredients = row[3]

class RecipeDB(db.DBbase):
    def reset_or_create_db(self):
        sql = """
        DROP TABLE IF EXISTS Recipe;
        
        CREATE TABLE Recipe (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            name TEXT,
            category varchar(20) NOT NULL,
            ingredients TEXT
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
                    
                    INSERT INTO Recipe (
                        id,
                        name ,
                        category ,
                        ingredients 
                    )
                    VALUES(?,?,?,?)
                    
                    """, (item.id, item.name, item.category, item.ingredients))

                    super().get_connection.commit()
                    print("Saved to DB:", item.id, item.name)

                except Exception as e:
                    print(e)
                    print("Save to DB aborted")


# Usage example
recipe_db = RecipeDB("RecipeDB.sqlite")
recipe_db.reset_or_create_db()
recipe_db.read_recipe_data("recipes.csv")
recipe_db.save_to_db()

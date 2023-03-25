import recipe
import csv


# class to break down a row into individual elements/columns
class Ingredients:
    def __init__(self, row):
        self.id = row[0]
        self.recipe_id = row[1]
        self.ingredient_name = row[2]
        self.quantity = row[3]


# class with functions for CRUD implementation for ingredients table
class IngredientsDB(recipe.RecipeDB):

    # function to drop and re-create ingredients table
    def reset_or_create_db(self):
        sql = """
        DROP TABLE IF EXISTS Ingredients;
        
        CREATE TABLE Ingredients (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            recipe_id INT4,
            ingredient_name varchar(256),
            quantity varchar(256) NOT NULL,
            FOREIGN KEY(recipe_id) REFERENCES Recipes(id)
        );
        """

        super().execute_script(sql)
        try:
            pass
        except Exception as e:
            print(e)

    # function to read ingredients data from csv and add to a list
    def read_ingredients_data(self, file_name):
        self.ingredient_list = []

        try:
            with open(file_name, "r") as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    Ingredient = Ingredients(row)
                    self.ingredient_list.append(Ingredient)
        except Exception as e:
            print(e)

    # function to write ingredients data from list into Ingredients table
    def save_to_db(self):
        print("Number of ingredients saved:", len(self.ingredient_list))
        save = input("Do you want to save the ingredients to the database? (y/n)").lower()
        if save == "y":
            for item in self.ingredient_list:
                try:
                    super().get_cursor.execute("""
                    
                    INSERT INTO Ingredients(
                        id,
                        recipe_id,
                        ingredient_name,
                        quantity
                    )
                    VALUES(?,?,?,?)

                    """, (item.id, item.recipe_id, item.ingredient_name, item.quantity))

                    super().get_connection.commit()
                    print("Saved to DB:", item.id, item.recipe_id)

                except Exception as e:
                    print(e)
                    print("Save to DB aborted")

    # Function to insert a single record into Ingredients table
    def insert_single_record(self):
        print("Insert a new ingredient record:\n")
        recipe_id = input("Recipe ID: ")
        ingredient_name = input("Ingredient Name: ")
        quantity = input("Quantity: ")
        try:
            super().get_cursor.execute("""
                INSERT INTO Ingredients(recipe_id, ingredient_name, quantity)
                VALUES (?,?,?)
            """, (recipe_id, ingredient_name, quantity))
            super().get_connection.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print(e)
            print("Failed to insert record.")

    # Function to retrieve a single record from Ingredients table
    def get_by_id(self, id):
        try:
            super().get_cursor.execute("SELECT * FROM Ingredients WHERE id=?", (id,))
            row = super().get_cursor.fetchone()
            if row:
                return Ingredients(row)
            else:
                print(f"No record found with id {id}.")
        except Exception as e:
            print(e)
            print(f"Failed to get record with id {id}.")

    # Function to retrieve a multiple records from Ingredients table corresponding to a recipe id
    def get_by_recipe_id(self, recipe_id):
        try:
            if id is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE recipe_id = ?",
                                                  (recipe_id,)).fetchall()
            else:
                return super().get_cursor.execute("SELECT * FROM Ingredients").fetchall()
        except Exception as e:
            print("An error has occurred.", e)

    # Function to retrieve a update a single record into the Ingredients table
    def update_record(self, id):
        try:
            # Get the current record from the database
            super().get_cursor.execute("SELECT * FROM Ingredients WHERE id=?", (id,))
            current_record = super().get_cursor.fetchone()
            if not current_record:
                print(f"No record with id {id} found.")
                return

            # Get the new values for the record
            new_recipe_id = input("Enter new recipe id (leave blank to keep current value): ")
            new_ingredient_name = input("Enter new ingredient name (leave blank to keep current value): ")
            new_quantity = input("Enter new quantity (leave blank to keep current value): ")

            # Update the record in the database
            sql = "UPDATE Ingredients SET recipe_id=?, ingredient_name=?, quantity=? WHERE id=?"
            params = (new_recipe_id or current_record[1], new_ingredient_name or current_record[2],
                      new_quantity or current_record[3], id)
            super().get_cursor.execute(sql, params)
            super().get_connection.commit()

            print(f"Record with id {id} updated successfully.")
        except Exception as e:
            print(e)
            print(f"Failed to update record with id {id}.")

    # Function to delete a single record from Ingredients table
    def delete_by_id(self, id):
        try:
            super().get_cursor.execute("DELETE FROM Ingredients WHERE id=?", (id,))
            super().get_connection.commit()
            print(f"Record with id {id} deleted successfully.")
        except Exception as e:
            print(e)
            print(f"Failed to delete record with id {id}.")

# initial class and function calls
# ingredients_db = IngredientsDB("RecipeDB.sqlite")
# ingredients_db.reset_or_create_db()
# ingredients_db.read_ingredients_data("ingredients.csv")
# ingredients_db.save_to_db()

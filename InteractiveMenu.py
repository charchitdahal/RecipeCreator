# import three scrips
import recipe
import ingredient
import user


class InteractiveMenu:

    def run(self):

        print("Welcome to RECIPE CREATOR AND MANAGER")

        # authenticate a user via user name a password
        user_db = user.UserDB("RecipeDB.sqlite")
        trial = ''
        while trial != 'n':
            user_name = input("Enter User Name: ")
            user_password = input("Enter Password")
            trial = 'n'
            if user_db.get_user_name_by_name(user_name) == '' or user_password != user_name + 'pass':
                trial = input("Incorrect username and password. Try again? (y/n)")

        # if the user is authentic..
        if (user_db.get_user_name_by_name(user_name) != '') and (user_password == user_name + 'pass'):

            # retrieve user's role
            user_role = user_db.get_user_role_by_name(user_name)

            # show options to the user based on his role
            if user_role == 'user':
                recipe_options = {
                    "1": "Display all available dishes on the menu",
                    "2": "Display ingredients by recipe_id",
                    "0": "Exit program"
                }
            elif user_role == 'admin':
                recipe_options = {
                    "1": "Display all available dishes on the menu",
                    "2": "Display ingredients by recipe_id",
                    "3": "Add a new dish",
                    "4": "Add ingredients for a dish",
                    "5": "Delete an existing dish and it's ingredients",
                    "6": "Update ingredients",
                    "7": "Delete ingredients",
                    "8": "Add a new user",
                    "9": "Delete an existing user",
                    "10": "Reset database",
                    "0": "Exit program"
                }

            user_selection = ""
            while user_selection != "0":
                print("*** Option List ***")
                for option in recipe_options.items():
                    print(option)

                user_selection = input("Select an option: ").lower()
                recipe_db = recipe.RecipeDB("RecipeDB.sqlite")
                ingredients_db = ingredient.IngredientsDB("RecipeDB.sqlite")
                user_db = user.UserDB("RecipeDB.sqlite")

                # Display all available dishes on the menu
                if user_selection == "1":
                    results = recipe_db.fetch_recipe()
                    for item in results:
                        print(item)
                    input("Press return to continue")

                # Display ingredients by recipe_id
                elif user_selection == "2":
                    recipe_id = int(input("Enter Recipe Id: "))
                    results = ingredients_db.get_by_recipe_id(recipe_id)
                    for item in results:
                        print(item)
                    input("Press return to continue")

                # Add a new dish
                elif user_selection == "3" and user_role == 'admin':
                    input("Press return to display list of existing dishes")
                    results = recipe_db.fetch_recipe()
                    for item in results:
                        print(item)

                    recipe_id = int(input("Enter Id for the new Recipe: "))
                    recipe_name = input("Enter name for the new Recipe: ")
                    recipe_category = input("Enter category for the new Recipe: ")

                    recipe_db.add_recipe(recipe_id, recipe_name, recipe_category)

                # Add ingredients for a dish
                elif user_selection == "4" and user_role == 'admin':
                    user_input_ingredient = input("Do you want to continue (y/n): ").lower()
                    while user_input_ingredient != "n":
                        ingredients_db.insert_single_record()
                        user_input_ingredient = input("Do you want to continue (y/n): ").lower()

                    input("Press return to continue")

                # Delete an existing dish and it's ingredients
                elif user_selection == "5" and user_role == 'admin':
                    input("Press return to display list of existing dishes")
                    results = recipe_db.fetch_recipe()
                    for item in results:
                        print(item)

                    recipe_id = int(input("Enter Id for the dish you would like to delete: "))

                    user_input_delete_dish = input(
                        "Do you want to continue deleting the dish and it's ingredients? (y/n): ").lower()
                    if user_input_delete_dish == "y":
                        recipe_db.delete_recipe(recipe_id)

                    input("Press return to continue")

                # Update ingredients
                elif user_selection == "6" and user_role == 'admin':
                    recipe_id = int(input("Enter Recipe Id for which you would like to update the ingredients: "))
                    results = ingredients_db.get_by_recipe_id(recipe_id)
                    for item in results:
                        print(item)
                    input("Press return to continue")

                    ingredient_id = int(input("Enter Ingredient Id: "))
                    ingredients_db.update_record(ingredient_id)

                    input("Press return to continue")

                # Delete ingredients
                elif user_selection == "7" and user_role == 'admin':
                    recipe_id = int(input("Enter Recipe Id for which you would like to delete the ingredients: "))
                    results = ingredients_db.get_by_recipe_id(recipe_id)
                    for item in results:
                        print(item)
                    input("Press return to continue")

                    ingredient_id = int(input("Enter Ingredient Id: "))

                    user_input_delete_ingredient = input(
                        "Do you want to continue deleting the ingredient? (y/n): ").lower()
                    if user_input_delete_ingredient == "y":
                        ingredients_db.delete_by_id(ingredient_id)

                    input("Press return to continue")


                # Add a new user
                elif user_selection == "8" and user_role == 'admin':

                    user_id = input("Enter New User's id: ")
                    user_name = input("Enter New User's Name: ")
                    role = input("Enter New User's Role: ")
                    user_db.add_user(user_id, user_name, role)

                    input("Press return to continue")

                # Delete an existing user
                elif user_selection == "9" and user_role == 'admin':

                    user_id = input("Enter New User's id: ")
                    user_input_delete_user = input("Do you want to continue deleting the user? (y/n): ").lower()
                    if user_input_delete_user == "y":
                        user_db.delete_user(user_id)

                    input("Press return to continue")


                # Reset database
                elif user_selection == "10" and user_role == 'admin':
                    confirm = input("This will delete all records in parts and inventory, continue? (y/n)").lower()
                    if confirm == "y":
                        recipe_db.reset_or_create_db()
                        ingredients_db.reset_or_create_db()
                        user_db.reset_or_create_db()
                        print("Reset complete")
                    else:
                        print("Reset aborted")
                    input("Press return to continue")

                else:
                    if user_selection != "exit":
                        print("Invalid selection, please try again\n")
                    input("Press return to continue")


# create an object of InteractiveMenu class
menu = InteractiveMenu()
# run the run() method to trigger the RECIPE CREATOR AND MANAGER program
menu.run()

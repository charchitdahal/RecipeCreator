# import three scrips
import recipe
import ingredient
import user


class InteractiveMenu:

    def run(self):
        recipe_options = {
            "getRecipe": "Display all available dishes on the menu",
            "getIngredients": "Display ingredients by recipe_id",
            "addRecipe": "Add a new dish",
            "deleteRecipe": "Delete an existing dish",
            "addIngredients": "Add ingredients for a dish",
            "updateIngredients": "Update ingredients",
            "deleteIngredients": "Update ingredients",
            "addUser": "Add a new user",
            "deleteUser": "Delete an existing user",
            "reset": "Reset database",
            "exit": "Exit program"
        }

    print("Welcome to RECIPE CREATOR AND MANAGER\nplease choose a selection")


menu=InteractiveMenu()
menu.run()
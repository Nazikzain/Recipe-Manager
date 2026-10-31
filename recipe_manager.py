
# ==================================================
# PROJECT: RECIPE MANAGER
# Description: A complete recipe management system
# ==================================================

import json
from pathlib import Path


# ==================================================
# FILE CONFIGURATION
# ==================================================

# Get the project directory
BASE_DIR = Path(__file__).resolve().parent

# Create the data directory path
DATA_DIR = BASE_DIR / "data"

# Create the JSON file path
DATA_FILE = DATA_DIR / "recipes.json"


# ==================================================
# GLOBAL DATA
# ==================================================

recipes = []


# ==================================================
# FUNCTION 1: SAVE RECIPES
# ==================================================

def save_recipes():

    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(recipes, file, indent=4, ensure_ascii=False)

        return True

    except OSError as error:
        print("Error saving recipes:", error)
        return False


# ==================================================
# FUNCTION 2: LOAD RECIPES
# ==================================================

def load_recipes():

    global recipes

    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        if not DATA_FILE.exists():
            recipes = []
            save_recipes()
            return

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

        if not isinstance(loaded_data, list):
            raise ValueError("Recipe data must be a list.")

        for recipe in loaded_data:
            if not isinstance(recipe, dict):
                raise ValueError("Invalid recipe data found.")

            required_keys = {
                "title",
                "ingredients",
                "instructions",
                "category"
            }

            if not required_keys.issubset(recipe):
                raise ValueError("A recipe is missing required fields.")

            if not isinstance(recipe["title"], str):
                raise ValueError("Invalid recipe title.")

            if not isinstance(recipe["ingredients"], list):
                raise ValueError("Invalid recipe ingredients.")

            if not all(
                isinstance(item, str)
                for item in recipe["ingredients"]
            ):
                raise ValueError("Invalid ingredient found.")

            if not isinstance(recipe["instructions"], str):
                raise ValueError("Invalid instructions.")

            if not isinstance(recipe["category"], str):
                raise ValueError("Invalid category.")

        recipes = loaded_data

    except (OSError, json.JSONDecodeError, ValueError) as error:
        recipes = []
        print("Error loading recipes:", error)
        print("Starting with an empty recipe list.")


# ==================================================
# FUNCTION 3: ADD A NEW RECIPE
# ==================================================

def add_recipe():

    print("\n===== ADD A NEW RECIPE =====")

    title = input("Enter recipe title: ").strip()

    if not title:
        print("Recipe title cannot be empty!")
        return

    ingredients_input = input(
        "Enter ingredients separated by commas: "
    )

    ingredients = [
        item.strip()
        for item in ingredients_input.split(",")
        if item.strip()
    ]

    if not ingredients:
        print("You must enter at least one ingredient!")
        return

    instructions = input(
        "Enter cooking instructions: "
    ).strip()

    if not instructions:
        print("Instructions cannot be empty!")
        return

    category = input(
        "Enter recipe category: "
    ).strip()

    if not category:
        print("Category cannot be empty!")
        return

    recipe = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "category": category
    }

    recipes.append(recipe)

    if save_recipes():
        print("\nRecipe added and saved successfully!")


# ==================================================
# FUNCTION 4: VIEW ALL RECIPES
# ==================================================

def view_recipes():

    print("\n===== ALL RECIPES =====")

    if not recipes:
        print("No recipes found.")
        return

    for index, recipe in enumerate(recipes, start=1):

        print(f"\nRecipe #{index}")
        print("------------------------------")

        print("Title:", recipe["title"])

        print("Ingredients:")

        for ingredient in recipe["ingredients"]:
            print("-", ingredient)

        print("Instructions:", recipe["instructions"])
        print("Category:", recipe["category"])

        print("------------------------------")


# ==================================================
# FUNCTION 5: SEARCH RECIPES
# ==================================================

def search_recipe():

    print("\n===== SEARCH RECIPES =====")

    if not recipes:
        print("No recipes available to search.")
        return

    search_term = input(
        "Enter recipe title or ingredient: "
    ).strip().lower()

    if not search_term:
        print("Please enter a search term.")
        return

    found_recipes = []

    for recipe in recipes:

        title = recipe["title"].lower()

        ingredients = [
            ingredient.lower()
            for ingredient in recipe["ingredients"]
        ]

        if (
            search_term in title
            or any(
                search_term in ingredient
                for ingredient in ingredients
            )
        ):
            found_recipes.append(recipe)

    if found_recipes:

        print("\n===== SEARCH RESULTS =====")

        for recipe in found_recipes:

            print("\nTitle:", recipe["title"])
            print("Ingredients:", ", ".join(recipe["ingredients"]))
            print("Category:", recipe["category"])
            print("Instructions:", recipe["instructions"])

    else:
        print("No matching recipes found.")


# ==================================================
# FUNCTION 6: EDIT A RECIPE
# ==================================================

def edit_recipe():

    print("\n===== EDIT A RECIPE =====")

    if not recipes:
        print("No recipes available to edit.")
        return

    view_recipes()

    try:
        recipe_number = int(
            input("\nEnter recipe number to edit: ")
        )

        if recipe_number < 1 or recipe_number > len(recipes):
            print("Invalid recipe number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    recipe = recipes[recipe_number - 1]

    print("\nPress Enter to keep the current value.")

    new_title = input(
        f"New title [{recipe['title']}]: "
    ).strip()

    if new_title:
        recipe["title"] = new_title

    new_ingredients = input(
        "New ingredients (separated by commas): "
    ).strip()

    if new_ingredients:
        ingredients = [
            item.strip()
            for item in new_ingredients.split(",")
            if item.strip()
        ]

        if ingredients:
            recipe["ingredients"] = ingredients
        else:
            print("Ingredients were not changed.")

    new_instructions = input(
        "New instructions: "
    ).strip()

    if new_instructions:
        recipe["instructions"] = new_instructions

    new_category = input(
        f"New category [{recipe['category']}]: "
    ).strip()

    if new_category:
        recipe["category"] = new_category

    if save_recipes():
        print("\nRecipe updated successfully!")


# ==================================================
# FUNCTION 7: DELETE A RECIPE
# ==================================================

def delete_recipe():

    print("\n===== DELETE A RECIPE =====")

    if not recipes:
        print("No recipes available to delete.")
        return

    view_recipes()

    try:
        recipe_number = int(
            input("\nEnter recipe number to delete: ")
        )

        if recipe_number < 1 or recipe_number > len(recipes):
            print("Invalid recipe number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    recipe = recipes[recipe_number - 1]

    confirmation = input(
        f"Are you sure you want to delete "
        f"'{recipe['title']}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        recipes.pop(recipe_number - 1)

        if save_recipes():
            print("\nRecipe deleted successfully!")

    else:
        print("Delete operation cancelled.")


# ==================================================
# FUNCTION 8: MAIN MENU
# ==================================================

def main_menu():

    while True:

        print("\n")
        print("=" * 45)
        print("          RECIPE MANAGER")
        print("=" * 45)

        print("1. Add a New Recipe")
        print("2. View All Recipes")
        print("3. Search for a Recipe")
        print("4. Edit a Recipe")
        print("5. Delete a Recipe")
        print("6. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_recipe()

        elif choice == "2":
            view_recipes()

        elif choice == "3":
            search_recipe()

        elif choice == "4":
            edit_recipe()

        elif choice == "5":
            delete_recipe()

        elif choice == "6":
            print("\nThank you for using Recipe Manager!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    load_recipes()

    print("\nWelcome to Recipe Manager!")

    main_menu()

# Recipe Manager

## Project Overview
Recipe Manager is a Python command-line application that helps users organise cooking recipes. Users can add, view, search, edit and delete recipes. Recipe data is stored in a JSON file so it remains available after the application is closed.

## Features
- Add a recipe with a title, ingredients, instructions and category.
- View all saved recipes.
- Search recipes by title or ingredient.
- Edit an existing recipe.
- Delete a recipe after confirmation.
- Save and load recipe data using JSON.
- Validate user input and handle common errors.
- Navigate through a menu-driven command-line interface.

## Technologies and Python Concepts
- Python 3
- Variables and data types
- Lists and dictionaries
- Functions
- `if`, `elif` and `else` statements
- `for` and `while` loops
- List methods such as `append()` and `pop()`
- String methods such as `strip()` and `lower()`
- Exception handling with `try` and `except`
- JSON and file handling
- `pathlib` for file paths

## Project Structure

```text
Recipe Manager/
├── recipe_manager.py
└── data/
    └── recipes.json
```

The `recipes.json` file is created automatically when the application first runs.

## Requirements
- Python 3 installed on your computer.
- No third-party packages are required.

## How to Run
1. Open the `Recipe Manager` folder in Visual Studio Code or a terminal.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python recipe_manager.py
   ```

4. Follow the on-screen menu.

If you are using Windows and the `python` command is not recognised, try:

```powershell
py recipe_manager.py
```

## Menu Options
1. Add a New Recipe
2. View All Recipes
3. Search for a Recipe
4. Edit a Recipe
5. Delete a Recipe
6. Exit

## Data Storage
Recipes are stored in `data/recipes.json`. The application loads the file at startup and saves changes after adding, editing or deleting a recipe.

## Testing
The application should be tested by:
- Adding a recipe and checking that it appears in the recipe list.
- Searching by a full or partial title and by an ingredient.
- Editing a recipe and checking the updated values.
- Deleting a test recipe and confirming the deletion.
- Closing and reopening the application to confirm that saved recipes are still available.
- Entering invalid menu choices and invalid recipe numbers.

## Challenges and Solutions
- **Keeping data between runs:** JSON file storage was used to save and reload recipes.
- **Handling user input:** Input checks and exception handling help prevent invalid values from crashing the application.
- **Finding recipes efficiently:** The search function checks both recipe titles and ingredient names, without depending on letter case.
- **Editing and deleting the correct recipe:** Recipes are displayed with numbered positions so the user can select the intended record.

## Limitations and Future Improvements
- The application currently uses a command-line interface.
- Recipe records are stored locally in one JSON file.
- Possible improvements include recipe ratings, preparation time, serving size, category filters, data export, and a graphical user interface.

## Author
Student Project – Python Programming

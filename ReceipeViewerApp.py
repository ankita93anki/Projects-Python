#Recipe Viewer App

#Step 1: Loas Receipes from file
def load_recipes(file_path):
    try: 
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            return recipes
    except FileNotFoundError:
        print("File not found.")
        return {}

#Step 2:Display recipe Menu
def show_menu():
    print("\n--- Recipe Viewer Menu ---")
    print("1. View Recipe by name")
    print("2. List All Recipes")
    print("3. Exit")

#Step 3: Display Recipe Details
def view_recipe(recipes):
    name  = input("Enter the name of the recipe: ").strip()
    if name in recipes:
        print(f"\n--- Recipe {name} Details ---")
        print(f"Name: {name}")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print("Recipe not found.")

#Step 4:Main Program
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        view_recipe(recipes)
    elif choice == '2':
        print("\n--- All Recipes ---")
        for name in recipes:
            print(name)
    elif choice == '3':
        print("Exiting the program.")
        break

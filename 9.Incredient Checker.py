coordinates = (10,20,30)
x,y,z = coordinates
print(x)
print(y)
print(z)

fruits = ("apple","banana","cherry")
print(len(fruits))

fruits = fruits + ("orange",)
print(fruits)

my_set = {1,2,3}
ingredients = {"flour","sugar","butter"}
print(ingredients)

ingredients.add("eggs")

ingredients.remove("sugar")

print(ingredients)

print("eggs" in ingredients)

set_a = {"flour","sugar","butter"}
set_b = {"sugar","eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

#Ingredient Checker

#Step 1: Define the recipe ingredients
recipe_ingredients = {"flour","sugar","butter", "eggs","milk"}

#step 2: Get user input for available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

#step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

#Step 4: Display the result
print("\n---- Ingredient Check Results -----")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("you have all the ingredients needed.")

print(f"Extra Ingredients: {extra_ingredients}")
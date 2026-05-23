#Tuples
fruits = ("apple","banana","cherry")
print(len(fruits))
print(fruits + ("orange",))

#set
my_set = {1,2,3}
ingredients = {"flour","sugar","butter"}
print(ingredients)
ingredients.add("bread")
print(ingredients)

set_a = {"flour","sugar","butter"}
set_b = {"sugar","eggs"}

print(set_a | set_b)  # union of element {'sugar', 'butter', 'flour', 'eggs'}
print(set_a & set_b) #  common element {'sugar'}
print(set_a - set_b) # unique element of set a {'butter', 'flour'}
print(set_a  ^ set_b) # unique element of both {'butter', 'eggs', 'flour'}


#Ingredient Checker

#Step1: Define the recipe ingredients
receipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

#step2: Get the user input for  available ingredients
user_input = input("Enter the ingredients you have (separated by comas :)")
user_ingredients  = set(user_input.split(", "))

#step3: Compare ingredients 
missing_ingredients = receipe_ingredients - user_ingredients
extra_ingredients =user_ingredients - receipe_ingredients

#step 4 Display the results
print("\n--- Ingredient check Results----")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed")

if extra_ingredients:
    print(f"You have extra ingredients: {''.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed")
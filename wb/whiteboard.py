# You have a recipe that serves a certain number of people, and you want to create a function that takes this recipe, the number of servings it produces, and the number of people to serve as input, and adjusts the recipe quantities accordingly.
# Write a Python function called adjust_recipe() that takes three arguments:
# 1) recipe (dictionary):
# A dictionary representing the original recipe.
# Each key-value pair should contain the following information:
# ingredient (string): The name of the ingredient.
# quantity (float): The quantity of the ingredient required for the recipe, in cups.
# 2) original_servings (integer): An integer representing the number of people the original recipe serves.
# 3) new_servings (integer): An integer representing the number of people to serve with the adjusted recipe.
# The function should return a new dictionary containing the adjusted ingredient quantities.
# Here’s an example of the input and output :
# base_recipe = {
#       ‘flour’: 2,
#       ‘sugar’: 1,
#       ‘butter’: 0.5,
#       ‘eggs’: 2
# }
# INPUT : (base_recipe, 4, 6) - This means the base recipe is made to serve 4 people and you want
# to adjust it for 6 people.
# OUTPUT: {
#     ‘flour’: 3,
#     ‘sugar’: 1.5,
#     ‘butter’: 0.75,
#     ‘eggs’: 3
#         }

base_recipe = {
      'flour': 2,
      'sugar': 1,
      'butter': 0.5,
      'eggs': 2
}

def adjust_recipe(orig_recipe, orig_serv, new_serv):
    new_serv_dict = {}
    ratio = new_serv / orig_serv
    for ingredient, amount in orig_recipe.items():
        new_serv_dict[ingredient] = amount * ratio
    return new_serv_dict

print(adjust_recipe(base_recipe, 4, 10))

recipe = {'chicken breast': 500, 'olive oil': 50, 'garlic': 2, 'lemon juice': 25}

print(adjust_recipe(recipe, 4, 2))

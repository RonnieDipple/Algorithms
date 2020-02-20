#!/usr/bin/python

import math
# Receives two dictionaries looking like:
#{
#'eggs': 5,
#'butter': 10,
#'sugar': 8,
#'flour': 15
#}
# recipe dictionary: key is the name and value is the amount which represents the amount of the ingredient needed for the recipe
# ingredient dictionary: key is the name and value is amount of ingredients you have

def recipe_batches(recipe, ingredients):
  #Thank you jack on this one
  totalCount=[]
  if recipe.keys()!=ingredients.keys():#if recipe key does not equal ingredient key return 0
    return -0
  for key, value in ingredients.items():# loops through looking for key and value in ingredient items
    print(f"recipe {recipe[key]} ingredient {value}")

    result = value//recipe[key]

    totalCount.append(result)
  totalCount.sort()
  return totalCount[0]


    #so the recipe comes in saying we need this many and type of ingredient for the recipe
    # then we do a for loop over the ingredients dictionary looking for the ingredient that the recipe wants
    # if we don't have enough ingredients or they don't exist in the ingredient dictionary return 0
    # if we can make the recipe, return the amount of times it can be made




if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

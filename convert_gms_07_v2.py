"""Takes external csv and converts amount in ml to gms
Version 2
Created by Joshua Kan
16/06/2021
"""

import csv

# Open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# Read data from above into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (First item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

complete_list = False
while not complete_list:
    amount = eval(input("How much? "))

    # Get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    if ingredient in food_dictionary:
        factor = food_dictionary.get(ingredient)
        amount = amount * float(factor) / 250
        print("amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

# Comment out loop for testing
#     another_item = input("\nPress <enter> to add another item \n"
#                          "or any key + <enter> to end: \n")
#     if not another_item:
#         continue
#     else:
#         complete_list = True


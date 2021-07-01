"""Second version of a combined converter using a function
Converts amount to mls and (if possible) converts mls to gms
Version 2
Created by Joshua Kan
24/06/2021
"""

import csv

def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= float(factor) / conversion_factor
        converted = "Yes"
    else:
        converted = "No"

    return [amount, converted]


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # Ask user for unit
    unit_to_check = input("Unit? ")

    # Abbreviation Lists
    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T", "tablespoons"]
    ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl", "quart", "quarts"]
    ml = ["milliliter", "millilitre", "cc", "mL", "milliliters", "mililitres", "mls"]
    litre = ["liter", "litre", "L", "liters", "litres"]
    decilitre = ["deciliter", "decilitre", "dL", "deciliters", "decilitres"]
    pound = ["lb", "lbs", "#", "pound", "pounds"]

    if not unit_to_check:
        # No need to print it out still need to return it
        return unit_to_check

    elif unit_to_check in teaspoon:
        return "teaspoon"
    elif unit_to_check in tablespoon:
        return "tablespoon"
    elif unit_to_check in ounce:
        return "ounce"
    elif unit_to_check in cup:
        return "cup"
    elif unit_to_check in pint:
        return "pint"
    elif unit_to_check in quart:
        return "quart"
    elif unit_to_check in ml:
        return "ml"
    elif unit_to_check in litre:
        return "litre"
    elif unit_to_check in decilitre:
        return "decilitre"
    elif unit_to_check in pound:
        return "pound"
    else:
        return unit_to_check # If the unit is not in this list

# Main Routine
#  Set up dictionary
unit_dict = {
    "teaspoon": 5,
    "tablespoon": 25,
    "cup": 250,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "decilitre": 100,
    "ml": 1
}

# Set up dictionary of conversion factors for ingredients
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
    # Ask user for amount
    amount = eval(input("How much? "))

    # Get unit and change it to match the dictionary
    unit = unit_checker()

    # Get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    # Convert to mls if possible
    amount = general_converter(amount, unit, unit_dict, 1)

    # If converted to mls, try to convert to grams
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # If the ingredient is in the list, convert it to grams
        if amount_2[1] == "yes":
            print(round(amount_2[0], 1), "grams")
        # If the ingredient is not in the conversion dicitonary, leave as ml
        else:
            print(round(amount[0], 1), "mls (Ingredient not in conversion dictionary)")

    # If the unit is not mls - leave line unchanged
    else:
        print(round(amount[0], 1), unit, "(Unable to convert to gms)")

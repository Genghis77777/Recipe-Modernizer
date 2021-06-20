"""Get amount and unit from user then check if unit is in dictionary of units
If it is, convert to mls, otherwise leave as is
Version 1
Created by Joshua Kan
15/06/2021
"""



#  Set up dictionary
unit_dict = {
    "tsp": 5,
    "tbsp": 25,
    "cup": 250,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

# Ask user for amount
amount = eval(input("How much? "))

# Ask user for unit
unit = input("Unit? ")

# Check if the unit is in the dictionary
# If unit in dictionary, convert to ml
# If no unit given or unit is unknown, leave as is
if unit in unit_dict:
    factor = unit_dict.get(unit)
    amount *= factor
    print("amount in ml {}".format(amount))
else:
    print("{} in unchanged".format(amount))

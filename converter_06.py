"""Initial version of a combined converter using a function (Component 8?)
Converts amount to mls but doesn't yet include conversion of mls to gms.
Version 1
Created by Joshua Kan
17/06/2021
"""

def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= factor * conversion_factor

    return amount


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # Ask user for unit
    unit_to_check = input("Unit? ")

    # Abbreviation Lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T"]
    ounce = ["oz", "fluid ounce", "fl oz"]
    cup = ["c"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl"]
    ml = ["milliliter", "millilitre", "cc", "mL"]
    litre = ["liter", "litre", "L"]
    decilitre = ["deciliter", "decilitre", "dL"]
    pound = ["lb", "lbs", "#"]

    if not unit_to_check:
        print("You chose no unit")
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
    "decilitre": 100
}

complete_list = False
while not complete_list:
    # Ask user for amount
    amount = eval(input("How much? "))

    # Get unit and change it to match the dictionary
    unit = unit_checker()

    # Check if the unit is in the dictionary
    # If unit in dictionary, convert to ml
    # If no unit given or unit is unknown, leave as is
    amount = general_converter(amount, unit, unit_dict, 1)
    print(amount)

    # To end the loop of items to check
    another_item = input("\nPress <enter> to add another item \n"
                         "or any key + <enter> to end:\n")
    if not another_item:
        continue
    else:
        complete_list = True

"""Recipe moderniser - full working program (version 9)
Changes to formatting - variable names and line lengths - to meet PEP8
Created by Joshua Kan
30/06/2021
"""

# Modules to be used
import csv
import re


# FUNCITONS
# Fuction to round numbers appropriately
def round_amount(amount_to_round):
    if amount_to_round % 1:  # Finds whole numbers
        amount_to_round = int(amount_to_round)  # and converts to integer
    elif amount_to_round * 10 % 1 == 0:
        amount_to_round = "{:.1f}".format(amount_to_round)  # and rounds to 1dp
    else:
        amount_to_round = "{:.2f}".format(amount_to_round)
        # Everthing else is rounding to 2dp

    return amount_to_round


# Prevents invalid blank input
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False
    num_ok = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        response = input(question)
        if not num_ok:  # Set to False
            for letter in response:  # Check for digits in recipe name
                if letter.isdigit():  # Tests for True - by default
                    number = True  # Sets true if any digit found

    # generate error for blank name of digits
    if not response or number is True:
        print(error)

    else:  # no error found
        return response  # return bypasses the need to set 'valid' to True.


# Number checking function
# Get's the scale factor - which must be a number
def num_check(question):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            response = eval(response)
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)  # Allows inappropriate value to be entered
        except NameError:
            print(error)  # Allows unrecognised name
        except SyntaxError:
            print(error)  # Show error rather than crashing if data-type wrong


def get_scale_factor():
    keep_scale_factor = False
    # Get serving size
    serving_size = num_check("\nWhat is the recipe serving size? "
                             "Enter 1 if unsure: ")
    # Get desired number of servings
    desired_size = num_check("How many servings are needed? "
                             "Enter 1 if unsure: ")
    # Calculate scale factor
    factor = desired_size / serving_size

    while not keep_scale_factor:
        # Warn the user if the scale factor is less than 0.25 or more than 4
        if factor < 0.25:
            print("Scale factor is {}".format(factor))
            print("Warning: This scale factor is very small and you \n"
                  "might struggle to accurately weigh the ingredients.\n"
                  "Please consider using a larger scale factor and freezing "
                  "the left-overs.")
            change_scale_factor = input("Press <Enter> to keep it, or <any "
                                        "other key> + <Enter> to change ")
            if not change_scale_factor:
                break
            else:
                factor = get_scale_factor()

        elif factor < 4:
            print("Scale factor is {}".format(scale_factor))
            print("Warning: This scale factor is quite large so you \n"
                  "might have issues with mixing bowl volumes and oven space."
                  "\nPlease consider using a smaller scale factor and making "
                  "more than one batch.")
            change_scale_factor = input("Press <Enter> to keep it, or <any "
                                        "other key> + <Enter> to change ")
            if not change_scale_factor:
                break
            else:
                factor = get_scale_factor()

        else:
            keep_scale_factor = True

    return factor


# Fuction to get (and check) amount, unit and ingredient
def get_all_ingredients():
    ingredient_list = []  # Set up ingredient list
    valid_list = False
    print("\nEnter ingredient on one line - qty, unit, then name (or 'X' to "
          "exit): \n")
    line_number = 1  # To make entering the ingredients easy to follow
    while not valid_list:
        # Calls the not_blank function and provides the question
        ingredient_name = not_blank("Ingredient line {}: ".format(line_number),
                                    "Ingredient can't be blank",
                                    True).lower()
        if ingredient_name != "X":  # Check for escape code
            ingredient_list.append(ingredient_name)  # If exit code not entered
            # add ingredient to list
            line_number += 1
        else:
            if len(ingredient_list) < 2:
                # Check that list contains at least two items
                print("Please enter at least two ingredients")
            else:
                return ingredient_list  # Output list


def general_converter(amount2, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount2 *= float(factor) / conversion_factor
        converted = "Yes"
    else:
        converted = "No"

    return [amount2, converted]


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker(raw_unit):
    # Ask user for unit
    unit_to_check = raw_unit

    # Abbreviation Lists
    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T", "tablespoons"]
    ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces", "oz."]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl", "quart", "quarts"]
    ml = ["milliliter", "millilitre", "cc", "mL", "milliliters", "mililitres",
          "mls"]
    litre = ["liter", "litre", "L", "liters", "litres"]
    decilitre = ["deciliter", "decilitre", "dL", "deciliters", "decilitres"]
    pound = ["lb", "lbs", "#", "pound", "pounds", "lb.", "lbs."]
    grams = ["g", "gram", "gms", "grams", "gm"]

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
        return unit_to_check  # If the unit is not in this list


def instructions():
    print()
    print("******* Instructions ********")
    print(
        "This program converts recipe ingredients to mls / grams and also \n"
        "allows users to up-size or down-size ingredients.")
    print()
    print("The program will ask for the source of the recipe - we recommend \n"
          "typeing in the URL where you found the recipe or the book where \n"
          "if is from so that you cna refer back to the original if necassary."
          "")
    print()
    print(
        "The program also asks for the number of servings. If you are not sure"
        ",\n"
        "type '1'. Then it asks for sercings required, you can increase\n"
        "or decrease the amount (eg 2 or 1/2) and the program will scale the "
        "\n"
        "ingredient amounts for you.")
    print()
    print("Not that you can use fractions if needed. For example, write \n"
          "one half as 1/2 adn one and three quarters as 1 3/4")
    print()
    print("Please only type in ONE ingredient per line, if a recipe says \n"
          "'butter or margarine', chooses ONE ingredient, either butter \n"
          "or margarine.")
    print()
    print("Lastly, all lines should start with a number / fraction unless \n"
          "no number is given <eg: a pinch of salt>.")
    print()
    print("**********")
    print()


# MAIN ROUTINE
# Set up dictionary
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
    "ml": 1,
    "gm": 1
}

# To check for errors in numeric entry of quantity
problem = False

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

# Set up list to hold 'modernised' ingredients
modernised_recipe = []

# Providing option for new user to get instructions
print("******** Welcome to the Great Recipe Moderniser ********")
print()

get_instructions = input(
    "Press <enter> to get instrucitons, or any other key + <enter>\n"
    "if you have used this program before: ")

if not get_instructions:
    instructions()
else:
    print()

# Get recipe name and check it is not blank and contians no numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank, or contain numbers!",
                        False)  # 'False' disallows digits in name

# Get recipe source and check it's not blank - numbers OK
# Customisable error message eg to include mention of numbers
source = not_blank("Where is the recipe from? ",
                   "The recipe source cant' be blank!",
                   True)  # 'True' allows digits in name

# Get serving sizes and desired number of servings
scale_factor = get_scale_factor()

# Get ingredients
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient
# The regex format below is expecting: number <space> number
# Need to have the r before the docstring to make it a raw string rather than
# a string literal (to pass PEP8 Tests)
mixed_regex = r"\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, /d{1,3} allows 1-3 digits, /s for space, \/ for divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # Get amount
    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()
        # .group returns the part of the string where there was a match

        # Replace the space in the mixed number with '+' sign
        amount = mixed_num.replace(" ", "+")

        # Changes the string into a float using python's evalution method
        amount = eval(amount) * scale_factor  # Scales the quantity as required

        # Get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        # Compiles the regex into a string object - so we can search for
        # patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # Produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient[1]).strip()
        # Removes the extra white space before and after the unit,
        # 2nd element in list, converting it into a string

    else:
        # Splits the line at the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # Convert amount to float if possible
            amount = amount * scale_factor
        except NameError:  # NameError rather than ValueError
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
        except SyntaxError:  # If amount unrecognised eg 1/ instead of 1/2
            problem = True
            modernised_recipe.append(recipe_line)
            continue
        unit_ingredient = get_amount[1]

    # Get unit and ingredient
    # Splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    unit = get_unit[0]  # Making the 1st item in the list 'unit'

    # Count the number of spaces in the recipe
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:  # Item has both unit and ingredient
        unit = get_unit[0]
        ingredient = get_unit[
            1]  # Making the 2nd item in the list 'ingredient'
        unit = unit_checker(unit)

        # If unit is already grams, add to list
        if unit == "gm":
            modernised_recipe.append("{:.0f} gm {}".format(amount, ingredient))
            continue

        # Convert to mls if possible: unit_dict gives amount in ml so
        # conversion factor is 1
        amount = general_converter(amount, unit, unit_dict, 1)

        # If converted to mls is 'True', try to convert to grams
        if amount[1]:
            amount_2 = general_converter(amount[0], ingredient,
                                         food_dictionary, 250)

            # If 'True' the ingredient is in the food_dictionary, so converts
            # it to grams
            if amount_2[1]:
                modernised_recipe.append(
                    "{:.0f} gm {}".format(amount_2[0], ingredient))
                # If only 2 elements (no unit) then just 2 variables needed

            # If the ingredinet is not in the food dictionary, leave as ml
            else:
                modernised_recipe.append(
                    "{:.0f} ml {}".format(amount_2[0], ingredient))

        # If the unit is not in mls, leave the line unchanged
        else:
            amount[0] = round_amount(amount[0])
            modernised_recipe.append(
                "{} {} {}".format(amount[0], unit, ingredient))

    # To cope with ingredient not requiring a unit value eg "3 eggs"
    else:
        amount = round_amount(amount)
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))

# Ouput details of recipe
print("\n************ {} ************".format(recipe_name))
print("Source: {}\n".format(source))
print("***** Ingredients - scaled by a factor of {} *****\n".format(
    scale_factor))

if problem:
    print("***** Warning ******")
    print("Some of the entries below might be incorrect as \n"
          "there were problems procesesing some of your inputs.\n"
          "Its possibel that you typed a fraction incompletely.")
    print()

# Output modernised recipe
for item in modernised_recipe:
    print(item)

"""Recipe moderniser - full working program (version 4)
Incorporates ingredients list splitter (component 9)
Created by Joshua Kan
23/06/2021
"""

# Modules to be used
import csv
import re

# FUNCITONS
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False
    num_ok = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        response = input(question)
        if not num_ok:   # Set to False
            for letter in response:  # Check for digits in recipe name
                if letter.isdigit():  # Tests for True - by default
                    number = True  # Sets true if any digit found

        if not response or number == True:  # generate error for blank name of digits
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
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

def get_scale_factor():
    keep_scale_factor = False
    while not keep_scale_factor:

        # Get serving size
        serving_size = num_check("What is the recipe serving size? ")
        # Get desired number of servings
        desired_size = num_check("How many servings are needed? ")
        # Calculate scale factor
        scale_factor = desired_size / serving_size

        # Warn the user if the scale factor is less than 0.25 or more than 4
        if scale_factor < 0.25:
            print("Scale factor is {}".format(scale_factor))
            print("Warning: This scale factor is very small and you \n"
                  "might struggle to accurately weigh the ingredients.\n"
                  "Please consider using a larger scale factor and freezing the"
                  " left-overs.")
            change_scale_factor = input("Press <Enter> to keep it, or <any other "
                                        "key> + <Enter> to change ")
            if not change_scale_factor:
                keep_scale_factor = True

        elif scale_factor < 4:
            print("Scale factor is {}".format(scale_factor))
            print("Warning: This scale factor is quite large so you \n"
                  "might have issues with mixing bowl volumes and oven space.\n"
                  "Please consider using a smaller scale factor and making more "
                  "than one batch.")
            change_scale_factor = input("Press <Enter> to keep it, or <any other "
                                        "key> + <Enter> to change ")
            if not change_scale_factor:
                keep_scale_factor = True

        else:
            keep_scale_factor = True

    return scale_factor

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
                                    True).title()
        if ingredient_name != "X":   # Check for escape code
            ingredient_list.append(ingredient_name)   # If exit code not entered
            # add ingredient to list
            line_number += 1
        else:
            if len(ingredient_list) < 2:  # Check that list contains at least two items
                print("Please enter at least two ingredients")
            else:
                valid_list = True  # If list contains 2 items break out of loop
                return ingredient_list  # Output list

# MAIN ROUTINE

# Set up dicitonaries

# Set up list to hold 'modernised' ingredients
modernised_recipe = []

# Get recipe name and check it is not blank and contians no numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank, or contain numbers!",
                        False)  # 'False' disallows digits in name

# Get recipe source and chekc it's not blank - numbers OK
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
# Need to have the r before the docstring to make it a raw string rather than a string literal (to pass PEP8 Tests)
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
        # Compiles the regex into a string object - so we can search for patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # Produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient [1]).strip()
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

        unit_ingredient = get_amount[1]

    # Get unit and ingredient
    # Splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    unit = get_unit[0]  # Making the 1st item in the list 'unit'

    # Count the number of spaces in the recipe
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:  # Item has both unit and ingredient
        unit = get_unit[0]
        ingredient = get_unit[1]  # Making the 2nd item in the list 'ingredient'
        # All 3 elements of the original recipe line are now broken into the 3 required variables
        modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))
        # To cope with ingredient not requiring a unit value eg "3 eggs"
    else:
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))


# Convert to ml
# Convert from ml to gm
# Add updated ingredient list

# Output modernised recipe
for item in modernised_recipe:
    print(item)

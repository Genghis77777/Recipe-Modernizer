"""Recipe moderniser - full working program
Gets recipe name and recipe source (components 1 and 2)
Version 1 - includes 'To Do' list
Created by Joshua Kan
21/06/2021
"""

# Modules to be used
import csv

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

# MAIN ROUTINE

# Set up dicitonaries

# Set up list to hold 'modernised' ingredients

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

# Get ingredients
# Loop for each ingredient...
# Get ingredient amount
# Scale amount using scale factor
# Get ingredient name and check its not blank and doesn't contain numbers
# Get unit
# Convert to ml
# Convert from ml to gm
# Add updated ingredient list

# Output modernised recipe


"""Get recipe name from user, checking that input doesn't contain numbers
and is not left blank
Created by Joshua Kan
Version 2 - 03/06/2021
"""


# Function to get recipe name and check it contains no digits
def not_blank(question):
    error = "Your recipe name is blank or contains a digit"
    valid = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        response = input(question)

        for letter in response:  # Check for digits in recipe name
            if letter.isdigit():  # Tests for True - by default
                number = True  # Sets true if any digit found

        if not response or number == True:  # generate error for blank name of digits
            print(error)

        else:  # no error found
            valid = True
            return response


# Main Routine
recipe_name = not_blank("What is the recipe name? ")
print("You are making {}".format(recipe_name))

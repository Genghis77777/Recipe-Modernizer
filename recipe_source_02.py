"""Get recipe source from user, checking that input is not left blank
and allowing user to allow or disallow digits
Created by Joshua Kan
08/06/2021
"""

# Function to get recipe name and check it contains no digits
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


# Main Routine
source = not_blank("What is the recipe name? ",
                   "The recpe source can't be blank! or include any numbers/floats!",  # Customisable error message eg to include mention of numbers
                   True)   # Can change this to "False" to disallow numbers in URL - need to change error mgs above too
print("You are making {}".format(source))

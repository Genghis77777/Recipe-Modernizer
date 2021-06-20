"""Get ingredients required to make recipe, adding them to a list
and then printing the list at the end
Created by Joshua Kan
10/06/2021
"""


# Set up ingredient list
def not_blank(question):
    error = "Please enter an ingredient name (cannot be blank)"
    valid = False

    while not valid:
        response = input(question)

        if not response:   # Checks if response has been entered
            print(error)   # And if not generates the error message

        else:   # Where no error found
            return response


# Main Routine
ingredient_list = [] # Set up ingredient list
valid_list = False
while not valid_list:
    ingredient_name = not_blank("Enter ingredient name (or 'X' to exit): ")\
        .title()   # calls the not_blank function and provides question
    if ingredient_name != "X":   # Check for escape code
        ingredient_list.append(ingredient_name)   # If exit code not entered
        # add ingredient to list
    else:
        if len(ingredient_list) < 2:   # Check that list contains at least two items
            print("Please enter at least two ingredients")
        else:
            valid_list = True   # If list contains 2 items break out of loop
            print("Here are your ingredients:\n()".format(ingredient_name))

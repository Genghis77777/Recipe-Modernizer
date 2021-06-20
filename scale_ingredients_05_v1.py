"""Get the scale factor, then the ingredient and amount required for each
Then add the ingredients with their scaled amounts into a list to be printed
at the end.
Created by Joshua Kan
14/06/2021
"""

# Number checking function
# Get's the scale factor - which must be a number
def num_check(question):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            if response <= 0:
                response = float(input("Please enter a number more than 0: "))
                
            else:
                return response
        except ValueError:
            print(error)


# Ask user for ingredient name
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

# Replace line below with component 3 (number checking function) in due course
scale_factor = float(input("Scale Factor: "))
ingredient_list = []   # Set up ingredient list
valid_list = False

while not valid_list:

    amount = input("Enter amount (or 'X' to exit): ")
    if amount.upper() != "X":
        if not amount or not amount.isdigit():   # Won't allow blank or strings
            print("Please enter a valid amount")
        else:
            amount = float(amount)  # Converts amount to a float
            scaled = num_check(amount) * scale_factor
            ingredient_name = not_blank("Enter ingredient name: ".title())
            # Calls the not_blank function and provides the question
            ingredient_list.append("{} units {}".format(scaled, ingredient_name))
            # Puts both elements on the same line
    elif len(ingredient_list) > 1:
        valid_list = True
        # If list contains at least two items break out of loop
        print("Here are your ingredients: ")
        for item in ingredient_list:
            print(item)  # Output list

    else:
        print("Please enter at least two ingredients")


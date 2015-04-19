# tryme3.py
# Written for Python 3.4.2
# Revision date: 2/24/15

# By: A. Programmer

#---------------------------------------------------------------------------------------
# This program is an experiment with functions
# the functions nine_lines and clear_screen are defined
# to show how functions can be used to make programming work easier
#---------------------------------------------------------------------------------------

# This function defines a new line
def new_line():
    print()

# This functions make three blank lines
def three_lines():
    new_line()
    new_line()
    new_line()

#This function makes nine blank lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# This function prints 25 blank lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# Using a function to print out 9 blank lines
print ("Now printing nine lines.")
nine_lines()

# Using a function to print out 25 blank lines
print ("Now printing 25 lines.")
clear_screen()
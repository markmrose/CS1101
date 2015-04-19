# mycalc.py
# Written for Python 3.4.2
# Revision date: 3/3/2015

# By: A. Programmer

#---------------------------------------------------------------------------------------
# This program is a simple Python calculator that performs +, -, * or /
# on two numbers entered by the user.
# This program will exit if text is entered in place of a number.
# This program will catch errors such as a 0 being entered and incorrect operator
#---------------------------------------------------------------------------------------

# Importing the decimal module to use later to make the numbers look 'better'

from decimal import *


# Definition of one function for this program

def new_line():
    print()


# Preamble to the calculator

print ("This is a simple Pythong calculator that takes two non-zero numbers")
print ("and will add (+), subtract (-), multiply (*), or divide (/) them depending")
print ("upon what symbol (+, -, *, or /) that you enter.")


# Setting up a while loop to run the algorithm over and over until the user wants to exit when later prompted

while True:
    new_line()

    # Input the first operand
    num1 = input ("Please input your first non-zero number: ")
    new_line()

    # Is the first operand a zero?  If so, try getting the correct input again.
    while float(num1)==0:
        print ("That number was a zero.")
        num1=input ("Please input your first non-zero number: ")
        new_line()

    # Input the second operand
    num2 = input ("Please input your second non-zero number: ")
    new_line()

    # Is the second operand a zero?  If so, try getting the correct input again.   
    while float(num2)==0:
        print ("That number was a zero.")
        num2=input ("Please input your second non-zero number: ")
        new_line()

    # Input the math operator and then check to see if it is a valid symbol
    operator = input ("Please enter the math operator such as +, -, * or /: ")
    new_line()
    while str(operator) not in {'+', '-', '*', '/'}:
        print ("That was not a valid operator.")
        operator=input ("Please input either +, -, *, or /: ")
        new_line()


    # Let's do the math.  I chose to use the decimal module to show the contextual amount of decimal places
    # I allowed for 28 decimal places just because I could
    
    if str(operator)=='+':
        getcontext().prec=28  # Setting my precision
        getcontext().rounding=ROUND_HALF_UP  #Rounds away from zero if the last sig digit is 5
        value = Decimal(num1)+Decimal(num2)  #Using decimal math here
        print (num1 + " " + operator + " " + num2 + " = ", value)
    elif str(operator)=='-':
        getcontext().prec=28
        getcontext().rounding=ROUND_HALF_UP
        value = Decimal(num1)-Decimal(num2)
        print (num1 + " " + operator + " " + num2 + " = ", value)
    elif str(operator)=='*':
        getcontext().prec=28
        getcontext().rounding=ROUND_HALF_UP
        value = Decimal(num1)*Decimal(num2)
        print (num1 + " " + operator + " " + num2 + " = ", value)
    else:
        getcontext().prec=28
        getcontext().rounding=ROUND_HALF_UP
        value = Decimal(num1)/Decimal(num2)
        print (num1 + " " + operator + " " + num2 + " = ", value)

    new_line()
    
    # Let's check to see if you want to do another problem and if not, exit the program

    cmd = input("Do you want to do another problem (Y/N)?: ")
    new_line()
    while str(cmd) not in {'Y', 'y', 'N', 'n'}:
        print ("That was not a valid answer.")
        cmd=input ("Please input either Y, y, N, or n: ")
        new_line()
    if str(cmd) in {'N', 'n'}:
        break

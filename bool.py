# bool.py
# Written for Python 3.4.3
# Revision date: 3/9/15

# By: A. Programmer

#---------------------------------------------------------------------------------------
# This program has a compare function for comparing two numbers
# Number num1 and num2 are entered and the function returns 1 if a>b,
# 0 if a==b, and -1 if a<b.  The user is prompted for the two numbers
# and the function is run and returns the result to the shell
#---------------------------------------------------------------------------------------

# This is the comparison function that takes two numbers and does some Boolean work to them

def compare(first_num, second_num):
    if int(first_num) < int(second_num):
        compare_answer = "-1"
        return compare_answer
    elif int(first_num) == int(second_num):
        compare_answer = "0"
        return compare_answer
    elif int(first_num) > int(second_num):
        compare_answer = "1"
        return compare_answer

# Another function to create blank lines

def new_line():
    print()

# Preamble to the boolean comparison
print ("This program does a Boolean comparison of two positive integers that you enter.")
print ("You will be prompted to enter 2 integers one at a time.")
print ("The program will compare those two numbers and respond with")
print ("-1 if number 1 is < number 2, 0 if number 1 == number 2, and 1 if number 1 > number 2.")

while True:
    new_line()

    # Input the first integer number for comparison
    num1 = input ("Please input your first positive integer: ")

    # Is the first number a positive integer?  If so, try getting the correct input again.
    while (num1.isdigit()) is False:
        print ("That number was not a positive integer.")
        num1=input ("Please input your first positive integer: ")

    # Input the second integer number for comparison
    num2 = input ("Please input your second positive integer: ")
    new_line()

    # Is the second number a positive integer?  If so, try getting the correct input again.
    while (num2.isdigit()) is False:
        print ("That number was not a positive integer.")
        num1=input ("Please input your second positive integer: ")

    answer_from_compare_function=compare(num1, num2)

    print ("     The return code from the comparison is:  " + answer_from_compare_function)
    new_line()

    # Let's check to see if you want to do another problem and if not, exit the program

    cmd = input("Do you want to do another problem (Y/N)?: ")

    #new_line()
    while str(cmd) not in {'Y', 'y', 'N', 'n'}:
        print ("That was not a valid answer.")
        cmd=input ("Please input either Y, y, N, or n: ")
        new_line()

    if str(cmd) in {'N', 'n'}:
        break


"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 3.1 Relational Operators
print("=" * 10, "Section 3.1 relational operators", "=" * 10)
# 1) Write a statement using the variables below and a
#    and a greater-than sign that will evaluate to true.
#    write a print statement with the statement in parentheses.
# 2) Write a statement using the variables below that
#    compares two of the variables to see if they are equal
#    write a print statement with the statement in parentheses.
# 3) Write a statement using the variables below that compares
#    two of the variables below to see if they are not equal
#    write a print statement with the statement in parentheses.
# 4) Write a statement using the variables below that uses
#    the less than or equal to operator
#    write a print statement with the statement in parentheses.

# variables
a = 6
b = 8
c = 5

# 1 sample answer
print(a > 3)

# 2

# 3

# 4

# TODO 3.2 the if else statement
print("=" * 10, "Section 3.2 if-else", "=" * 10)
# Add code below to determine if age is greater than or equal to 18
# Depending on the answer, display the appropriate statement:
#    "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structure
age = int(input("How old are you? "))

# TODO 3.3 comparing strings
print("=" * 10, "Section 3.3 comparing strings", "=" * 10)
# Complete the code below so that if the user input matches the password
# it will display "that is correct" otherwise display "that is not correct"
password = "narwhals"
user_password = input("Please enter the password:  ")

# TODO 3.4 if - elif - else
print("=" * 10, "Section 3.4 if-elif-else", "=" * 10)
# Complete the code to accept a number between 1 and 5 from the user
# and display a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement display "That is not a valid number"
number = int(input("Please enter a number between 1 and 5: "))

# TODO 3.5 a series of conditions
print("=" * 10, "Section 3.5 multiple conditions", "=" * 10)
# Buffet prices are based on the persons age. If the person is a senior
# citizen (62 or over) , the charge is $9.89. If the person is age 12-
# 61, the charge is $12.89. If it is a child of under age 3, they eat
# for free. If the child is between 4 and 11 they are charged $0.99 for
# each year of age. Complete the code below. SEE SAMPLE PAGE 132

customer_age = int(input("How old is the customer?   "))
cost = 0  # initializing cost, assign the correct price to this variable
# Complete the code here to determine the correct cost based on age


# Output, correctly formatted -- leave this code to display the result
print("Your cost for a customer who is " + str(customer_age) + " years old")
print("is $" + format(cost, ",.2f"))

# TODO 3.5 Logical Operators
print("=" * 10, "Section 3.5 logical operators", "=" * 10)
# Using the variables below, combine relational comparisons using logical operators
# 1) write a print statement using the and operator that will evaluate to true
# 2) write a print statement using the or operator that will evaluate to true
# 3) write a print statement using the not operator that will evaluate to true
d = 10
e = 10
f = 12


# TODO 3.6 Boolean variable
print("=" * 10, "Section 3.6 boolean variables", "=" * 10)
# You are programming a baby doll. If the baby doll is tired, it will close its eyes
# if it is hungry, it will cry. Write code to print  "Eyes open" or "Eyes closed" depending
# on the tired value. Then print "Crying" or "quiet" depending on the hungry variable
tired = True
hungry = False




# Assignment:
# Create a program that helps someone create a budget. It should ask the user for monthly income and  the following
# expenses:
# Housing
# Food
# Transportation
# Phone
# Utilities
# Clothing
# The program should get input from the user and convert each of the inputs to floats.
# The program should tell the user how much money they have left after it subtracts the budgeted items from the income.
# The program should calculate and display the income percentage of each budget item.

monthly_income = float(input("How much money do you earn per month on average?"))
housing = float(input("How much do you do you pay for housing?"))
food = float(input("How much do you spend on food?"))
transportation = float(input("How much do you spend on gas, car services and transportation?"))
phone = float(input("How much do you spend on your phone bill?"))
utilities = float(input("How much do you spend on utilities?"))
clothing = float(input("How much do you spend on clothing?"))

print("Your monthly income is $" + str(format(monthly_income, '.2f')))
print("You spend " + str(format(housing/monthly_income, '.2%')) + " on housing")
print("You spend " + str(format(food/monthly_income, '.2%')) + " on food")
print("You spend " + str(format(transportation/monthly_income, '.2%')) + " on transportation")
print("You spend " + str(format(phone/monthly_income, '.2%')) + " on your phone bill")
print("You spend " + str(format(utilities/monthly_income, '.2%')) + " on utilities")
print("You spend " + str(format(clothing/monthly_income, '.2%')) + " on clothing")
print("You are left with $" + str(format(monthly_income-housing-food-transportation-phone-utilities-clothing, '.2f')
                                  + " to spend"))

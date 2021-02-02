# Assignment:
# Find a recipe online, provide a link to the recipe in the comments. Display the ingredients with amounts and list the
# servings that will be made with the recipe. Ask the user to enter how many servings they would like to make, and
# display the required amount of ingredients they will need. Format to one decimal place
# Recipe from https://www.hersheys.com/kitchens/en_us/recipes/hersheys-perfectly-chocolate-chocolate-cake.html

serving = 12
sugar = 2
flour = 1.75
hershey_cocoa = .75
baking_powder = 1.5
baking_soda = 1.5
salt = 1
egg = 2
milk = 1
vegetable_oil = .5
vanilla_extract = 2
boiling_water = 1
print("This recipe serves 12")
desired_serving = input("How many servings would you like?")
multiply = int(desired_serving) / serving
print("This recipe requires: ")
print("Sugar: " + str(format(sugar*multiply, '.1f')) + " cups")
print("Flour: " + str(format(flour*multiply, '.1f')) + " cups")
print("Hershey's Cocoa: " + str(format(hershey_cocoa*multiply, '.1f')) + " cups")
print("Baking Powder: " + str(format(baking_powder*multiply, '.1f')) + " teaspoons")
print("Baking Soda: " + str(format(baking_soda*multiply, '.1f')) + " teaspoons")
print("Salt: " + str(format(salt*multiply, '.1f')) + " teaspoons")
print("Eggs: " + str(int(egg*multiply)))
print("Milk: " + str(format(milk*multiply, '.1f')) + " cups")
print("Vegetable Oil: " + str(format(vegetable_oil*multiply, '.1f')) + " cups")
print("Vanilla Extract: " + str(format(vanilla_extract*multiply, '.1f')) + " cups")
print("Boiling Water: " + str(format(baking_soda*multiply, '.1f')) + " cups")

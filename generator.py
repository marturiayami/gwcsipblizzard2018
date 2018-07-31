# #imports the ability to get a random number (we will learn more about this later!)
# from random import *
#
# #Create the list of words you want to choose from.
# aList = ["Catch", "Affinity", "Owen", "Strap", "Trainer", "Basketball", "Professor","Highlight", "Expansion", "Abaddon"]
#
# #Generates a random integer.
#
# print(aList[aRandomIndex])
# resp = input("Would you like a cool name? yes or no")
# while resp != "no":
#     if resp == "yes":
#         aRandomIndex = randint(0, len(aList)-1)
#         print(aList[aRandomIndex])
#     else:
#         print("{} is an invalid input".format(resp))
#     resp = input("Would you like a cool name? yes or no")

side = ["Mashed Potatoes", "Grits", "Potato Salad"]
main = ["Steak", "Mac n' Cheese", "Casserole"]
dessert = ["Flan", "Choco Strawberries", "Baked Alaska"]

resp = input("Would you like a course list? yes or no")
while resp != "no":
    if resp == "yes":
        aRandomIndex = randint(0, len(main)-1)
        print(main[aRandomIndex])
        brandindex = randint(0, len(side)-1)
        print(side[brandindex])
        crandindex = randint(0, len(dessert)-1)
        print(dessert[crandindex])
    else:
        print("{} is an invalid input".format(resp))
        resp = input("Would you like a course list? yes or no")

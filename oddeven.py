import random
def even_or_odd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd? ")
    if computer_value%2 == 0 and user_input == "even":
        print("YA DID IT! YOU SO SMORT!")
    if computer_value%2 == 0 and user_input == "odd":
        print("You're wrong.")
    if computer_value%2 != 0 and user_input == "odd":
        print("YA DID IT! YOU SO SMORT!")
    if computer_value%2 != 0 and user_input == "even":
        print("You're wrong.")

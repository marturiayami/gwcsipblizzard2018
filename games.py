# import the random module since you  will need it in your game functions
import random 
#TODO: define function guess_the_num

#TODO: define function rock_paper_scissors

#TODO: define function madlibs

#TODO: define function riddle
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


# Starter code for a riddle game
# The user has N tries to guess the answer to a riddle
# After the first attempt, give the user a hint for each attempt

def display(riddle, try_number, hint_list):
    '''
    Given the riddle and number of attempts, the function
    displays number of attempts and the riddle question
    input: riddle (string), try_number(integer), hint_list (list of strings)
    output (return value): N/A
    '''
    # TODO: Print the attempt number and the riddle question
    print(riddle)
    print("Number of guesses: {}".format(try_number).rstrip())
    # Print a hint if not the first attempt
    if try_number == 1:
        print("HINT: {}".format(hint_list[0])) # TODO: Access hint_list for a hints
    if try_number == 2:
        print("HINT: {}".format(hint_list[1]))


def riddle():
    # Initialize our variables
    guess_count = 0                   # Keeps track of the number of guesses (need if using a while loop)
    riddle = "What can run but can’t walk?"     # The riddle
    answer = "water" or "Water"                 # The answer to the riddle; can be a string or list of possible answers
    hints = ["It is everywhere", "You need it to live"]      # List of hints; number of hints == number of allowed attempts - 1
                                      # i.e. if 3 guesses allowed, need 2 hints
    guess = None                      # Keep track of the user's guess
    win = False                       # Keep track of whether the user has won

    # Use a loop that gives the user 3 tries to guess the answer to the riddle
    for attempt in range(0,3):
        # TODO: Call "display" function (with the right parameters!!)
        display(riddle, guess_count, hints)
        # and print out the riddle prompt, attempt number,
        # and hints if not the first try
        # TODO: Get user input and process it
        guess = input("Enter your guess: ").lower().rstrip()
        if answer != guess:
            guess_count += 1
        # TODO: Check if answer is correct
        if answer == guess:
            # TODO: Set variable "win" to True and break out of loop
            win = True
            break
    # TODO: Print different messages for winning and losing.
    while win != False:
        print("Congradulations the correct answer is {}.".format(answer))
        break
    while win != True:
        print("Sorry that is incorrect. The correct answer is {}. Good luck next time.".format(answer))
        break
    #       Be sure to include the right answer in your message
    #
    #      i.e. "Congrats! The answer is indeed _____" for winning,
    #      "WRRRROOOOONG. The correct answer is _____" for losing

#have a word/phrase
phrase = "turtles are cool"
#keep track of guesses
guessed_letters = []
game_over = False

#keep track of bad letters
bad = []
#keep track of good letters
good = []

#tells user the spaces/number of letters that need to be guessed
display = ""
for letter in phrase:
    if letter in guessed_letters:
      display += letter
      #processing the space in out phrase
    elif letter == " ":
        display += " "
    #the letter in our phrase has not been guessed yet
    else:
        display += "_ "
print(display)

while game_over != True:
    #allow user to give input to computer
    guess = input("Enter a letter: ")

    #tell the user if they get the right letter
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    #tell the user if they get the wrong letter
    else:
        print("{} is not in the phrase.".format(guess))
    guessed_letters.append(guess)

    #tells user the spaces/number of letters that need to be guessed
    display = ""
    for letter in phrase:
        if letter in guessed_letters:
          display += letter
          #processing the space in out phrase
        elif letter == " ":
            display += " "
        #the letter in our phrase has not been guessed yet
        else:
            display += "_ "
    print(display)

    game_over = True
    for d in display:
        if d == "_":
            game_over = False
print("END OF THE GAME!")

#end game is user guesses all the correct letters

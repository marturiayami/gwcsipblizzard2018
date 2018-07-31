# --- Define your functions below! ---
def intro():
    print("Welcome to the ChatBot!")
def art():
    print("""
    ***********                  ***********
  *****************            *****************
*********************        *********************
***********************      ***********************
************************    ************************
*************************  *************************
 **************************************************
  ************************************************
    ********************************************
      ****************************************
         **********************************
           ******************************
              ************************
                ********************
                   **************
                     **********
                       ******
                         ** \n You're the coolest ;)""")
def greeting():
    cool = input("hello! Would you like to see something cool? yes/no")
    if cool or again == "yes":
        art()
    elif cool or again == "no":
        print("Boooo! You're no fun!")
    else:
        again = input("Yo that wasn't an option, and your no fun so bye!")

def is_valid_input(response, all_valid):
    if response in all_valid:
        return True
    else:
        return False
def dating():
    print("""Hi, my name is Chloe. The 'C' and the 'L' are silent. In my freetime (which is all the time since I'm unemployed)
          I like long walks on the beach, leeching off my parents and adopting dogs I have no plans of taking care of.""")
    rep = input("Sooo, how about you? Come here often?")
    print("Actually nevermind I give up and I'm becoming a nun good luck with everthing.")

# --- Put your main program below! ---
def main():
    valid_input = ["Hello ;)", "love me", "Come here often?", "I need a partner in crime", "hi", "yes", "no", ]
    intro()

    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer == "hi":
                greeting()
            elif answer in ["Hello ;)", "love me", "Come here often?", "I need a partner in crime"]:
                dating()
        else:
            print("These are the inputs I understand: ")
            for vi in valid_input:
                print(vi)
            print("I don't understand anything else")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()

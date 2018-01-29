# Script that will run the quiz

import sys
import getpass

# These modules are in try/except statements to prevent errors from hapening 
# Since they don't belong to the standard library
try:
    from colorama import *
except ModuleNotFoundError as e:
    import os
    print("Please wait while we install neccessary modules")
    os.system("pip install colorama")

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

def start_play(quiz):
    print(Style.BRIGHT + "Welcome to the Quiz Player!")

    while True:
        print("What do you want to do?")
        print("1. Play {}".format(quiz.name))
        print(Fore.RED + Style.BRIGHT + "2. Exit\n")

        action = input()

        # Play quiz
        if action == "1":
            quiz.play()

        # Exit
        elif action == "2":
            getpass.getpass("Press Enter to exit . . .")
            sys.exit()

        else:
            print("You must input a 1 or 2!\n")

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")
    sys.exit(0)

# RANTS AND WISHES DOWN BELOW

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!
# Script that will run the quiz

import sys
import getpass
from QuizingCore import QuizPlayMode
from __init__ import CONST_version_number

# These modules are in try/except statements to prevent errors from hapening 
# Since they don't belong to the standard library
try:
    from colorama import *
except ModuleNotFoundError as e:
    os.system("pip install colorama")

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quiz Runner!")

# Variable to hold the quiz
quiz = None

def main():
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
            continue

# I want to make sure you first pass through QuizingProject.py (which has the functionaltiy to open the file and
# handle it to the Maker and Player)
if __name__ == "__main__":
    sys.exit(-1)

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!
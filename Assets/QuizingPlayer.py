import sys
import getpass
from colorama import *

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

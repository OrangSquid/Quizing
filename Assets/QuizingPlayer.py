# DONE! DO NOT TOUCH THIS! THIS SHIT IS REFACTOREd

import getpass
import os
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

def start_play(quiz):
    print(Style.BRIGHT + "Welcome to the Quiz Player!")

    while True:

        if quiz.settings["preview"]:
            preview = True

            print("What do you want to do?")
            print("1. Play {}".format(quiz.name))
            print("2. Preview")
            print(Fore.RED + Style.BRIGHT + "3. Exit\n")

        else:
            preview = False

            print("What do you want to do?")
            print("1. Play {}".format(quiz.name))
            print(Fore.RED + Style.BRIGHT + "2. Exit\n")

        action = input()

        # Play quiz
        if action == "1":
            quiz.play()

        # Preview
        elif action == "2" and preview:
            print(quiz)

        # Exit and preview off
        elif action == "2" and not preview:
            getpass.getpass("Press Enter to exit . . .")
            os.system("cls")
            return

        # Exit and preview on
        elif action == "3" and preview:
            getpass.getpass("Press Enter to exit . . .")
            os.system("cls")
            return
            
        else:
            print(Style.BRIGHT + Fore.RED + "You must input a valid number!\n")

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")

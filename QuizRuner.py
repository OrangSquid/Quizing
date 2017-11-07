import json
import sys
import getpass

# These modules are in try/except statements to prevent errors from hapening 
# Since they don't belong to the standard library
try:
    from QuizingCore import QuizPlayMode
except ModuleNotFoundError as e:
    print("\nAn error occured while importing QuizingCore.")
    print("Redownloading the program might be a possible solution.")
    print("Error:\n\n", e)
    getpass.getpass("Press Enter to exit . . . ")
    sys.exit()

try:
    from colorama import *
except ModuleNotFoundError as e:
    print("\nAn error occured while importing colorama.")
    print("Please be sure that you have colorama instaled using pip.")
    print("Error:\n\n", e)
    getpass.getpass("Press Enter to exit . . . ")
    sys.exit()

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

quiz = None

def main():
    print(Style.BRIGHT + "Welcome to the Quiz Runner!")
    try:
        with open("quiz.quiz", "r") as f:
            quiz_file = json.load(f)
            global quiz
            quiz = QuizPlayMode(quiz_file["name"], quiz_file["questions"], quiz_file["correct_answers"], quiz_file["settings"])
    except Exception as e:
        print("An error ocurred!\n")
        print(e)
        getpass.getpass("Press Enter to exit . . .")
        sys.exit()

    while True:
        print(
"""What do you want to do?
1. Play {}""".format(quiz.name))
        print(Fore.RED + Style.BRIGHT + "2. Exit\n")

        action = input()

        if action == "1":
            quiz.play()
        elif action == "2":
            getpass.getpass("Press Enter to exit . . .")
            sys.exit()
        else:
            print("You must input a 1 or 2!\n")
            continue

if __name__ == "__main__":
    main()

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!
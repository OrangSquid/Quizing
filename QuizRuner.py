import json
import sys
import getpass
from colorama import *
from QuizingCore import QuizPlayMode

init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quiz Runner!")

quiz = None

def main():
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

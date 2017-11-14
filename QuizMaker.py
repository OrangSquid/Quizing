# Script that will make the quiz

import json
import sys
import getpass
import os

# These modules are in try/except statements to prevent errors from hapening 
# Since they don't belong to the standard library
try:
    from QuizingCore import QuizCreateMode
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

print(Style.BRIGHT + "Welcome to the Quiz Maker!")

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quiz Maker!")

# Variable to hold the quiz
quiz = None

# Funtions that open up a file in the same directory with the name quiz.quiz
# If it doesn't exist, a new one will be created
def open_file():
    pass

def create_file():
    pass

def main():

    open_file()

    print("What do you want to do?")
    print()
    print("1. Change quiz settings")
    print("2. Check quiz")
    print("3. Add question")
    print("4. Delete question")
    print(Fore.RED + Style.BRIGHT + "5. Exit and save\n")
    
    action = input()

    # Change quiz settings
    if action == "1":
        # while loop to loop back if invalid number is inputed
        while True:
            print("What setting do you want to change?")
            print()
            print("1. Default number of options")
            print("2. Name of the quiz")
            print("3. Scoring system")
            print(Fore.RED + Style.BRIGHT + "4. Return\n")

            action == input()

            # Default number of options
            if action == "1":
                quiz.change__number_options()
                break

            # Name of the quiz
            elif action == "2":
                quiz.change__name()
                break

            # Scoring system
            elif action == "3":
                while True:
                    print("Do you want to change the wrong answer or right answer points?")
                    print()
                    print("1. Wrong")
                    print("2. Right")
                    print(Fore.RED + Style.BRIGHT + "3. Return\n")
                      
                    action = input()

                    if action == "1" or action == "2":
                        quiz.change__scoring(action)
                        break
                    else:
                        print(Fore.RED + Style.BRIGHT + "You must input a 1 or 2!\n")
                        continue

            # Return
            elif action == "4":
                getpass.getpass("Press Enter to return . . . ")
                break

            else:
                print(Fore.RED + Style.BRIGHT + "You must input a number!\n")
                continue
            
        # Reason #1
        main()

    # Check quiz
    elif action == "2":
        print(quiz)
        main()

    # Add question
    elif action == "3":
        question = input("What's the question?\n\n")
        while True:
            action = input("\nDo you want to use the default options number? It's {} [Y/N] ".format(self.settings["default options"])).upper()
            if action == "Y":
                self.add_question(self.settings["default options"], question)
                main()
            elif action == "N":
                while True:
                    try:
                        options = int(input("How many options do you want then? MAX 26:\n"))
                        if n < 1 or n > 27:
                            print(Fore.RED + Style.BRIGHT + "You must input a number between 2 and 26!\n")
                            continue
                        else:
                            break
                    except:
                        print(Fore.RED + Style.BRIGHT + "You must input a number between 2 and 26!\n")
                        continue
                quiz.add_question(options, question)
                del options
                del question
                main()
            else:
                print(Fore.RED + Style.BRIGHT + "You must input a Y or N!\n")
                continue
        #Reason #1
        main()
        
    # Delete question
    elif action == "4":
        while True:
            try:
                number = int(input("What question do you want to delete?"))
                break
            except:
                print(Fore.RED + Style.BRIGHT + "You must input a number!")
                continue
        quiz.delete_question(number)
        del number
        # Reason #1
        main()
        
    # Exit and save
    elif action == "5":
        with open(r"C:\Users\rafae\Desktop\quiz.quiz", "w") as f:
            json.dump({"name": quiz.name, 
                        "settings": quiz.settings, 
                        "questions": quiz.questions, 
                        "correct_answers": quiz.correct_answers}, f)
            getpass.getpass("Press Enter to exit . . .")
            sys.exit()

    else:
        print(Fore.RED + Style.BRIGHT + "You must input a number between 1 and 6!")
        # Reason #1
        main()

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!

# UPDATE: Hi me from the past and the future, this code is a mess and right now I'm fixing it
# I won't fix everything (obviously), but probably the me from the future will fix it. Right now is 7th November 2017, 20h51

# To stop reapiting the same reasons over and over, I made a list so that
# You can refer to here

# Reason #1
# This is in the middle of nowhere to make sure that after
# The user is done with this operation it returns right back into the main action "asker"
# (I couldn't come up with a better name)
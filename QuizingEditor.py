import sys
import getpass
import json

# This module is in a try/except statement to prevent errors from hapening 
# Since it doesn't belong to the standard library
try:
    from colorama import *
except ModuleNotFoundError as e:
    import os
    print("Please wait while we install neccessary modules")
    os.system("pip install colorama")

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)
    
def start_edit(quiz, file):

    print(Style.BRIGHT + "Welcome to the Quiz Editor!")
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

            action = input()

            # Default number of options
            if action == "1":
                quiz.change_number_options()
                break

            # Name of the quiz
            elif action == "2":
                quiz.change_name()
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
                        quiz.change_scoring(action)
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
            
        start_edit(quiz, file)

    # Check quiz
    elif action == "2":
        print(quiz)
        start_edit(quiz, file)

    # Add question
    elif action == "3":
        question = input("What's the question?\n\n")
        while True:
            action = input("\nDo you want to use the default options number? It's {} [Y/N] ".format(quiz.settings["default_options"])).upper()
            if action == "Y":
                quiz.add_question(quiz.settings["default_options"], question)
                start_edit(quiz, file)
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
                start_edit(quiz, file)
            else:
                print(Fore.RED + Style.BRIGHT + "You must input a Y or N!\n")
                continue
        start_edit(quiz, file)
        
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
        start_edit(quiz, file)
        
    # Exit and save
    elif action == "5":
        with open(file, "w") as f:
            json.dump({"name": quiz.name, 
                        "settings": quiz.settings, 
                        "questions": quiz.questions, 
                        "correct_answers": quiz.correct_answers}, f, indent="\t")
            getpass.getpass("Press Enter to exit . . .")
            sys.exit()

    else:
        print(Fore.RED + Style.BRIGHT + "You must input a number between 1 and 6!")
        start_edit(quiz, file)

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")

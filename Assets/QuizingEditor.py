import getpass
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)
    
def start_edit(quiz):

    while True:
        print(Style.BRIGHT + "Welcome to the Quiz Editor!")
        print("What do you want to do?\n")
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
                print("What setting do you want to change?\n")
                print("1. Default number of options")
                print("2. Name of the quiz")
                print("3. Scoring system")
                print("4. Shuffling")
                print("5. Preview")
                print(Fore.RED + Style.BRIGHT + "6. Return\n")

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
                        print("Do you want to change the wrong answer or right answer points?\n")
                        print("1. Wrong")
                        print("2. Right")
                        print(Fore.RED + Style.BRIGHT + "3. Return\n")
                      
                        action = input()

                        if action == "1" or action == "2":
                            quiz.change_scoring(action)
                            break
                    
                        elif action == "3":
                            break

                        else:
                            print(Fore.RED + Style.BRIGHT + "You must input a number between 1 and 3!\n")
                            continue

                # Shuffling
                elif action == "4":
                    while True:
                        print("Do you want to change the shuffling for questions or answers?\n")
                        print("1. Questions")
                        print("2. Answers")
                        print(Fore.RED + Style.BRIGHT + "3. Return\n")
                      
                        action = input()

                        if action == "1" or action == "2":
                            quiz.change_shuffling(action)
                            break

                        elif action == "3":
                            break

                        else:
                            print(Fore.RED + Style.BRIGHT + "You must input a number between 1 and 3!\n")
                            continue

                # Preview
                elif action == "5":
                    quiz.change_preview()
                    break

                # Return
                elif action == "6":
                    getpass.getpass("Press Enter to return . . . ")
                    break

                # Invlaid number
                else:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!\n")
                    continue

                # This break is to get the user to the "main" menu
                break

        # Check quiz
        elif action == "2":
            print(quiz)

        # Add question
        elif action == "3":
            question = input("What's the question?\n\n")
            while True:
                action = input("\nDo you want to use the default options number? It's {} [Y/N] ".format(quiz.settings["default_options"])).upper()
                if action == "Y":
                    quiz.add_question(quiz.settings["default_options"], question)
                    break
                elif action == "N":
                    while True:
                        try:
                            options = int(input("How many options do you want then? MAX 26:\n"))
                            if options <= 1 or options >= 26:
                                print(Fore.RED + Style.BRIGHT + "You must input a number between 2 and 26!\n")
                                continue
                            else:
                                break
                        except ValueError:
                            print(Fore.RED + Style.BRIGHT + "You must input a number between 2 and 26!\n")
                            continue
                    quiz.add_question(options, question)
                else:
                    print(Fore.RED + Style.BRIGHT + "You must input a Y or N!\n")
                    continue
        
        # Delete question
        elif action == "4":
            if quiz.questions == []:
                print("There are no questions to delete.")
                getpass.getpass("Press Enter to go back . . .")
            else:
                while True:
                    try:
                        print(quiz)
                        number = int(input("What question do you want to delete?"))
                        break
                    except:
                        print(Fore.RED + Style.BRIGHT + "You must input a number!")
                        continue
                quiz.delete_question(number)
        
        # Exit and save
        elif action == "5":
            break

    else:
        print(Fore.RED + Style.BRIGHT + "You must input a number between 1 and 6!")

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")
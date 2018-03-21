import os
import sys
import getpass
import json
import Assets.QuizingCore as QuizingCore
import Assets.QuizingEditor as QuizingEditor
import Assets.QuizingPlayer as QuizingPlayer
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quizing Project!\n")

# This is just for you ;)
class ThisBitchEmptyError(Exception):
    """YEEEEEETTTT"""
    pass

def main():

    def choose_path(**kwargs):
        """Diretcs the user to either QuizingEditor.py or QuzingPlayer.py"""
        try:
            with open(kwargs["file"], "r") as f:
                temp = json.load(f)
        except:
            file_exists = False
            print("Would you like to:\n")
            print("1. Make a Quiz")
            print(Fore.RED + Style.BRIGHT + "2. Exit")
        else:
            file_exists = True
            print("Would you like to:\n")
            print("1. Edit the Quiz")
            print("2. Play the Quiz")
            print(Fore.RED + Style.BRIGHT + "3. Exit\n")

        while True:
            action = input()

            # Make or Edit Quiz
            if action == "1":
                if not file_exists:
                    name = input("What will be the name of the file? ")
                    with open("{}.quiz".format(name), "w") as f:
                        json.dump(
                            {"name" : name,
                            "settings" : {},
                            "questions" : []}, f)
                    with open("{}.quiz".format(name), "r") as f:
                        temp = json.load(f)
                    quiz = QuizingCore.QuizCreateMode(temp["name"], 
                                             temp["settings"], 
                                             temp["questions"])
                    quiz.set_settings()
                else:
                    quiz = QuizingCore.QuizCreateMode(temp["name"], 
                                             temp["settings"], 
                                             temp["questions"])
                QuizingEditor.start_edit(quiz)

            # Play Quiz
            elif action == "2" and file_exists:
                quiz = QuizingCore.QuizPlayMode(temp["name"], 
                                       temp["settings"], 
                                       temp["questions"])
                QuizingPlayer.start_play(quiz)

            # Exit with nonexistent file
            elif action == "2" and not file_exists:
                getpass.getpass("Press Enter to exit . . .")
                sys.exit()

            # Exit with existent file
            elif action == "3":
                getpass.getpass("Press Enter to exit . . .")
                sys.exit()

            else:
                print("You must input a valid number!")

    # try/except block to check for console arguments and if they're valid
    # In case of failure 
    try:
        file = " ".join(sys.argv[1:])
        if file == "":
            raise ThisBitchEmptyError
        elif os.path.isfile(file) and file.endswith(".quiz"):
            print("File detected through console argument\n")
            choose_path(file = file)
        else:
            print(Fore.BRIGHT + Fore.RED + "Invalid file passed!\n")
            getpass.getpass("Press Enter to exit . . . ")
            sys.exit()
    except ThisBitchEmptyError:
       filenames = os.listdir(os.curdir)

       valid_options = []

       # Checks if file has a valid extension
       for filename in filenames:
           if os.path.isfile(filename) and filename.endswith(".quiz"):
               valid_options.append(filename)

       if valid_options == []:
           print("No file detected")
           choose_path()
       elif len(valid_options) == 1:
           print("File detected in current directory: {}".format(valid_options[0]))
           choose_path(file = valid_options[0])
       else:
           print("Multiple files detected in current directory")
           print("Please choose one!\n")
           option = 1
           for file in valid_options:
               print("{}. {}".format(option, file))
               option += 1
           while True:
               try:
                   option = int(input("\n"))
               except:
                   print("You must input a valid number!")
                   continue
               if option <= len(valid_options):
                   choose_path(file = valid_options[option - 1])

if __name__ == "__main__":
    main()
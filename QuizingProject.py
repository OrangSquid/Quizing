import os
import sys
import getpass
import json
from Assets import *
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quizing Project!\n")

def main():

    def choose_path(**kwargs):
        # Diretcs the user to either QuizingEditor.py or QuzingPlayer.py

        def save(file):
            # Saves the file after editing is finished in QuizingEditor
            with open(file, "w") as f:
                json.dump({"quiz_ver": 1.0,
                           "name": quiz.name, 
                           "settings": quiz.settings, 
                           "questions": quiz.questions}, f, indent = "\t")

        try:
            with open(kwargs["file"], "r") as f:
                temp = json.load(f)
        except KeyError:
            file_exists = False
            print("Would you like to:\n")
            print("1. Make a new Quiz")
            print(Fore.RED + Style.BRIGHT + "2. Exit\n")
        else:
            file_exists = True
            print("Would you like to:\n")
            print("1. Edit \"{}\"".format(temp["name"]))
            print("2. Play \"{}\"".format(temp["name"]))
            print(Fore.RED + Style.BRIGHT + "3. Exit\n")

        while True:
            action = input()

            # Make or Edit Quiz
            if action == "1":
                if not file_exists:
                    name = input("What will be the name of the file? ")
                    file_temp = "{}.jquiz".format(name)
                    with open(file_temp, "w") as f:
                        json.dump(
                            {"quiz_ver": 1.0,
                             "name" : name,
                             "settings" : {"scoring": {}},
                             "questions" : []}, f, indent = "\t")
                    with open("{}.jquiz".format(name), "r") as f:
                        temp = json.load(f)
                    quiz = QuizingCore.QuizEditMode(temp["name"], 
                                                    temp["settings"], 
                                                    temp["questions"])
                    quiz.set_settings()
                    # The save fuctions is called two times here to prevent unexpected exits 
                    # and prevent the .jquiz file to not have settings
                    save(file_temp)
                    QuizingEditor.start_edit(quiz)
                    save(file_temp)
                    choose_path(file = file_temp)
                else:
                    quiz = QuizingCore.QuizEditMode(temp["name"], 
                                                    temp["settings"], 
                                                    temp["questions"])
                    QuizingEditor.start_edit(quiz)
                    save(kwargs["file"])
                    choose_path(file = kwargs["file"])

            # Play Quiz
            elif action == "2" and file_exists:
                quiz = QuizingCore.QuizPlayMode(temp["name"], 
                                        temp["settings"], 
                                        temp["questions"])
                QuizingPlayer.start_play(quiz)
                choose_path(file = kwargs["file"])

            # Exit with nonexistent file
            elif action == "2" and not file_exists:
                getpass.getpass("Press Enter to exit . . .")
                sys.exit()
                break

            # Exit with existent file
            elif action == "3":
                getpass.getpass("Press Enter to exit . . .")
                sys.exit()
                break

            else:
                print(Style.BRIGHT + Fore.RED + "You must input a number between 1 and 4")
                continue

    file = " ".join(sys.argv[1:])
    # No file inputed
    if file == "":
        filenames = os.listdir(os.curdir)

        valid_options = []

        # Checks if file has a valid extension
        for filename in filenames:
            if os.path.isfile(filename) and filename.endswith(".jquiz"):
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
                except ValueError:
                    print(Style.BRIGHT + Fore.RED + "You must input a valid number!")
                    continue
                if option <= len(valid_options) and option >= 1:
                    choose_path(file = valid_options[option - 1])
                else:
                    print(Style.BRIGHT + Fore.RED + "You must input a valid number!")

    # Valid file
    elif os.path.isfile(file) and file.endswith(".jquiz"):
        print("File detected through console argument\n")
        choose_path(file = file)

    # Invalid file
    else:
        print(Fore.BRIGHT + Fore.RED + "Invalid file passed!\n")
        choose_path()


if __name__ == "__main__":
    main()
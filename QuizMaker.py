import json
import sys
import getpass
import codecs
from colorama import *
from QuizingCore import QuizCreateMode

init(autoreset = True)

quiz = None

def main():
    print(Style.BRIGHT + "Welcome to the Quiz Maker!")
    # Opens up a file in the same directory with the name quiz.json
    # If it doesn't exist, the script will create one
    def open_file():
        with open("quiz.quiz", "r") as f:
            global quiz
            try:
                quiz_file = json.load(f)
            except Exception as e:
                print("An error ocurred while reading your file")
                print("Please check the quiz.quiz file to see if it has atleast two curly brackets {}")
                print("If it didn't work please add this issue into the GitHub issue page\n")
                print(e, end = "\n")
                getpass.getpass("Press Enter to exit. . . ")
                sys.exit()
            if quiz_file == {}:
                with open("quiz.quiz", "w") as f2:
                    json.dump({"name": "", "settings": {}, "questions": {}, "correct_answers": []}, f2)
                with open("quiz.quiz", "r") as f2:
                    quiz_file = json.load(f2)
                quiz = QuizCreateMode(quiz_file["name"], quiz_file["questions"], quiz_file["correct_answers"], quiz_file["settings"])
                quiz.set_settings()
            else:
                quiz = QuizCreateMode(quiz_file["name"], quiz_file["questions"], quiz_file["correct_answers"], quiz_file["settings"])
    try:
        with open("quiz.quiz", "x") as f:
            json.dump({"name": "", "settings": {}, "questions": {}, "correct_answers": []}, f)
            print("Created new file!")
            print("""If you didn't want to create a new file, please check if the file you
want to wotk with has the name quiz.quiz""")
        open_file()
        quiz.set_settings()
    except:
        open_file()

    while True:
        print(
"""What do you want to do?

1. Change quiz settings
2. Check quiz
3. Add question
4. Delete question""")
        print(Fore.RED + Style.BRIGHT + "5. Exit and save\n")
        action = input()

        if action == "1":
            quiz.change_settings()

        elif action == "2":
            print(quiz)

        elif action == "3":
            quiz.add_question1()
        
        elif action == "4":
            while True:
                try:
                    n = int(input("What question do you want to delete?"))
                except:
                    print("You must input a number!")
                    continue
                    quiz.delete_question(n)
        
        elif action == "5":
            with open("quiz.quiz", "w") as f:
                json.dump({"name": quiz.name, 
                           "settings": quiz.settings, 
                           "questions": quiz.questions, 
                           "correct_answers": quiz.correct_answers}, f, ensure_ascii = False)
                getpass.getpass("Press Enter to exit . . .")
                sys.exit()

        else:
            print("You must input a number between 1 and 6!")

if __name__ == "__main__":
    main()

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!
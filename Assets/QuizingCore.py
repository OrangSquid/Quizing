import string
import getpass
import random
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

# Dicitonary to hold alphabet for quiz options
ALPHA_ORDER = dict(enumerate(string.ascii_uppercase, 1))
REVERSE_ALPHA_ORDER = reverse_alpha_order = dict(zip(ALPHA_ORDER.values(), ALPHA_ORDER.keys()))

class Quiz():
    def __init__(self, name, settings, questions):
        self.name = name
        self.settings = settings
        self.questions = questions

    # Method for printing the quiz
    def __str__(self):
        print(Style.BRIGHT + "QUIZ SETTINGS: \n")
        print("Default number question optitions: {}".format(self.settings["default_options"]))
        print("Wrong Answer points: {}".format(self.settings["scoring"]["incorrect"]))
        print("Right Answer points: {}".format(self.settings["scoring"]["correct"]))
        print("Shuffling questions: {}".format(self.settings["shuffle_questions"]))
        print("Shuffling answers: {}".format(self.settings["shuffle_answers"]))
        print("Timer: {}".format(self.settings["timer"]))
        print("Preview: {}".format(self.settings["preview"]))
    
        if self.questions == []:
            print("There are currently no questions")
        else:
            counter_questions = 1
            counter_answers = 1
            for x in self.questions:
                print("\nQuestion {}: {}\n".format(counter_questions, x["question"]))
                for y in x["answers"]:
                    if y["correct"]:
                        print(Style.BRIGHT + Fore.GREEN + "Option {}: {}".format(ALPHA_ORDER[counter_answers], y["option"]))
                    else:
                        print("Option {}: {}".format(ALPHA_ORDER[counter_answers - 1], y["option"]))
                    counter_answers += 1
                counter_questions += 1
        return ""

# Class Used in QuizingEditor.py
class QuizEditMode(Quiz):

    # DONE!
    def change_number_options(self, **kwargs):
        # kwargs accepts the variable "default_options"
        try:
            self.settings["default_options"] = kwargs["default_options"]
        except:
            print(Back.RED + Style.BRIGHT + "Please note that the current questions won't be affected!\n")
            try:
                self.settings["default_options"] = int(input("How many options do you want then?"))
            except:
                print(Fore.RED + Style.BRIGHT + "You must input a number !!\n")
                self.change.number_options()
        print("The default number of options was changed successfully!")

    # DONE!
    def change_name(self, **kwargs):
        # kwargs accepts the variable "name"
        try:
            self.name = kwargs["name"]
        except:
            self.name = input("What's the new name of the quiz? The current name is {}\n\n".format(self.name))
        print("Name changed successfully!")

    def change_scoring(self):
        if option == "1":
            while True:
                print("Right now, for each wrong question you get {}.".format(self.settings["scoring"]["incorrect"]))
                try:
                    self.settings["scoring"]["incorrect"] = int(input("How many points should the player get?"))
                    break
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
            print("Scoring system changed successufully!")

        else:
            while True:
                print("Right now, for each right question you get {}.".format(self.settings["scoring"]["correct"]))
                try:
                    self.settings["scoring"]["correct"] = int(input("How many points should the player get?"))
                    break
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
            print("Scoring system changed successufully!")

    def change_timer(self, time):
        self.settings["timer"] = time
        print("Timer changed successufully!")

    def change_shuffling(self, option):
        if option == "1":
            if self.settings["shuffle_questions"]:
                print("Right now, the shuffling for questions is on")
            else:
                print("Right now, the shuffling for questions is off")
            temp = input("Do you want to change it[Y/N]? ").lower()
            while temp != "y" or temp != "n":
                temp = input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
            if temp == "y":
                self.settings["shuffle_questions"] = not self.settings["shuffle_questions"]
            print("Shuffling system changed successufully!")

        else:
            if self.settings["shuffle_answers"]:
                print("Right now, the shuffling for answers is on")
            else:
                print("Right now, the shuffling for answers is off")
            temp = input("Do you want to change it[Y/N]? ").lower()
            while temp != "y" or temp != "n":
                temp = input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
            if temp == "y":
                self.settings["shuffle_answers"] = not self.settings["shuffle_answers"]
            print("Shuffling system changed successufully!")

    def change_preview(self):
        if self.settings["preview"]:
            print("Right now, the shuffling for questions is on")
        else:
            print("Right now, the shuffling for questions is off")
        temp = input("Do you want to change it[Y/N]? ").lower()
        while temp != "y" or temp != "n":
            temp = input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
        if temp == "y":
            self.settings["shuffle_questions"] = not self.settings["shuffle_questions"]
        print("Shuffling system changed successufully!")
    
    def add_question(self, number, question):
        question_temp = {"Question": question}
        for x in range(1, number + 1):
            question_temp["Option " +  ALPHA_ORDER[x]] = input("Option " + ALPHA_ORDER[x] + ". ")
        while True:
            correct = input("\nWhat option is the correct one? Write the letter: ").upper()
            for x in question_temp.keys():
                # The 7th index is where the letter is *
                if x[7] == correct:
                    break
            else:
                print(Fore.RED + Style.BRIGHT + "You must input the letter of the correct option!")
                continue
            break
        self.questions.append(question_temp)

    def edit_question(self, number):
        pass

    def delete_question(self, number):
        temp = self.questions.pop(number - 1)
        print(temp)

    def set_settings(self):
        # Default options number and scoring
        try:
            self.settings["default_options"] = int(input("How many options will be the default number? "))
            while self.settings["default_options"] >= 27 or self.settings["default_options"] <= 1:
                self.settings["default_options"] = int(input(Fore.RED + Style.BRIGHT + "The number must be between 2 and 26! "))
            w = int(input("How many points should the player get for each wrong answer?\n"))
            r = int(input("How many points should the player get for each right answer?\n"))
        except:
            print(Fore.RED + Style.BRIGHT + "You must input a number!")
            self.set_settings()
        self.settings["scoring"] = {"incorrect": w, "correct": r}

        # Shuffle questions
        temp = input("Shuffle questions? [Y/N] ").lower()
        while temp != "y" or temp != "n":
            input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
        if temp == "y":
            self.settings["shuffle_questions"] == True
        else:
            self.settings["shuffle_questions"] == True

        # Shuffle answers
        temp = input("Shuffle answers? [Y/N] ").lower()
        while temp != "y" or temp != "n":
            input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
        if temp == "y":
            self.settings["shuffle_answers"] == True
        else:
            self.settings["shuffle_answers"] == True

        # Timer
        while True:
            try:
                self.settings["timer"] = int(input("How much time do you want to answers each question? (0 = no timer) "))
                break
            except:
                print(Style.BRIGHT + Fore.RED + "You must input a number!")

        # Name
        self.name = input("What's the name of this quiz?\n")
        print("Setup successfull!")

# Class used in QuizingPlayer.py
# DONE!
class QuizPlayMode(Quiz):
        
    def play(self):
        print("Let's play!")

        temp = self.questions[:]
        score = 0
        got_right = 0

        if self.settings["shuffle_questions"]:
            random.shuffle(temp)
    
        if self.settings["shuffle_answers"]:
            for x in enumerate(temp):
                random.shuffle(temp[x[0]]["answers"])

        counter_questions = 1
        for question in temp:
            counter_answers = 1
            print("\nQuestion {}: {}\n".format(counter_questions, question["question"]))
            for option in question["answers"]:
                print("Option {}. {}".format(ALPHA_ORDER[counter_answers], option["option"]))
                counter_answers += 1
            while True:
                answer = input("\n? ").upper()
                try:

                    if question["answers"][REVERSE_ALPHA_ORDER[answer] - 1]["correct"]:
                        print(Style.BRIGHT + Fore.GREEN + "You're right!")
                        got_right += 1
                        score += self.settings["scoring"]["correct"]

                    else:
                        print(Style.BRIGHT + Fore.RED +  "You're wrong!\n")
                        score += self.settings["scoring"]["incorrect"]
                        counter_answers = 1
                        # Print correct answer with colors (insert unicorn puking rainbows)
                        for option in question["answers"]:
                            if question["answers"][REVERSE_ALPHA_ORDER[answer] - 1]["option"] == option["option"]:
                                print(Style.BRIGHT + Fore.RED + "Option {}. {}".format(ALPHA_ORDER[counter_answers], option["option"]))
                            elif option["correct"]:
                                print(Style.BRIGHT + Fore.GREEN + "Option {}. {}".format(ALPHA_ORDER[counter_answers], option["option"]))
                            else:
                                print("Option {}. {}".format(ALPHA_ORDER[counter_answers], option["option"]))
                            counter_answers += 1

                    counter_questions += 1
                    break
                    
                except:
                    print(Style.BRIGHT + Fore.RED + "\nInput a valid letter!")


        print(Style.BRIGHT + "\nEND!")
        getpass.getpass("You got {} answers right and {} points\n".format(got_right, score))

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")

# * Why the fuck didn't you first commented this
# I have been staring at this for a whole 10 minutes
# Trying to figure it out
# Dumbass
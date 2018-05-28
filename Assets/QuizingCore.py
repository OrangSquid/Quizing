import string
import getpass
import random
import copy
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

# Dicitonary to hold alphabet for quiz options
ALPHA_ORDER = dict(enumerate(string.ascii_uppercase, 1))
REVERSE_ALPHA_ORDER = dict(zip(ALPHA_ORDER.values(), ALPHA_ORDER.keys()))

# For invalid arguments passed through **kwargs
class InvalidArgumentError(Exception):
    pass

class Quiz():
    def __init__(self, name, settings, questions):
        self.name = name
        self.settings = settings
        self.questions = questions

    def __str__(self):
        print(Style.BRIGHT + "QUIZ SETTINGS: \n")
        print("Default number question optitions: {}".format(self.settings["default_options"]))
        print("Wrong Answer points: {}".format(self.settings["scoring"]["incorrect"]))
        print("Right Answer points: {}".format(self.settings["scoring"]["correct"]))
        print("Shuffling questions: {}".format(self.settings["shuffle_questions"]))
        print("Shuffling answers: {}".format(self.settings["shuffle_answers"]))
        print("Preview: {}".format(self.settings["preview"]))

# Class Used in QuizingEditor.py
class QuizEditMode(Quiz):

    # DONE!
    def change_number_options(self, **kwargs):
        # kwargs accepts the variable "default_options"
        try:
            if type(kwargs["default_options"]) == int:
                self.settings["default_options"] = kwargs["default_options"]
            else:
                raise InvalidArgumentError("The value inputed through the argument is not valid")
        except KeyError:
            print(Back.RED + "Please note that the current questions won't be affected!\n")
            print(Fore.YELLOW + "Current \"Default number of options\": {}".format(self.settings["default_options"]))
            while True:
                try:
                    self.settings["default_options"] = int(input("New vaule: "))
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a valid number !!\n")
                if self.settings["default_options"] > 26 or self.settings["default_options"] < 2:
                    print(Fore.RED + Style.BRIGHT + "You must input a number between 26 and 2!!\n")
                break
        print("The default number of options was changed successfully!\n")

    # DONE!
    def change_name(self, **kwargs):
        # kwargs accepts the variable "name"
        try:
            self.name = kwargs["name"]
        except:
            print(Fore.YELLOW + "Current \"Name\": {}".format(self.name))
            self.name = input("New value: ")
        print("Name changed successfully!\n")

    # DONE!
    def change_scoring(self, *args, **kwargs):
        """ kwargs accepts the variables "scoring_correct" and "scoring_incorrect"
        args is for the option of what the user wants to change in the cli"""
        try:
            if type(kwargs["scoring_incorrect"]) == int:
                self.settings["scoring"]["incorrect"] = kwargs["scoring_incorrect"]
            else:
                raise InvalidArgumentError("The value inputed through the argument is not valid")
        except KeyError:
            try:
                if type(kwargs["scoring_correct"]) == int:
                    self.settings["scoring"]["correct"] = kwargs["scoring_correct"]
                else:
                    raise InvalidArgumentError("The value inputed through the argument is not valid")
            except KeyError:
                if args[0] == "1":
                    while True:
                        print(Fore.YELLOW + "Current \"Incorrect scoring\": {}.".format(self.settings["scoring"]["incorrect"]))
                        try:
                            self.settings["scoring"]["incorrect"] = int(input("New value: "))
                            break
                        except:
                            print(Fore.RED + Style.BRIGHT + "You must input a number!")

                else:
                    while True:
                        print(Fore.YELLOW + "Current \"Correct scoring\": {}.".format(self.settings["scoring"]["correct"]))
                        try:
                            self.settings["scoring"]["correct"] = int(input("New value: "))
                            break
                        except:
                            print(Fore.RED + Style.BRIGHT + "You must input a number!")
        else:
            if type(kwargs["scoring_correct"]) == int:
                self.settings["scoring"]["correct"] = kwargs["scoring_correct"]
            else:
                raise InvalidArgumentError("The value inputed through the argument is not valid")
        print("Scoring system changed successufully!")

    # DONE!
    def change_shuffling(self, *args, **kwargs):
        """ kwargs accepts the variables "shuffle_questions" and "shuffle_answers"
        args is for the option of what the user wants to change in the cli"""
        try:
            if type(kwargs["shuffle_questions"]) == bool:
                self.settings["shuffle_questions"] = kwargs["shuffle_questions"]
            else:
                raise InvalidArgumentError("The value inputed through the argument is not valid")
        except KeyError:
            try:
                if type(kwargs["shuffle_answers"]) == bool:
                    self.settings["shuffle_answers"] = kwargs["shuffle_answers"]
                else:
                    raise InvalidArgumentError("The value inputed through the argument is not valid")
            except KeyError:
                if args[0] == "1":
                    if self.settings["shuffle_questions"]:
                        print(Fore.YELLOW + "Current \"Shuffling questions\": ON")
                    else:
                        print(Fore.YELLOW + "Current \"Shuffling questions\": OFF")
                    while True:
                        temp = input("Switch it? [Y/N]").lower()
                        if temp == "y":
                            self.settings["shuffle_questions"] = not self.settings["shuffle_questions"]
                            break
                        elif temp == "n":
                            break
                        else:
                            print(Fore.RED + Style.BRIGHT + "You must input a [Y/N]!")

                else:
                    if self.settings["shuffle_answers"]:
                        print(Fore.YELLOW + "Current \"Shuffling answers\": ON")
                    else:
                        print(Fore.YELLOW + "Current \"Shuffling answers\": OFF")
                    while True:
                        temp = input("Switch it? [Y/N]").lower()
                        if temp == "y":
                            self.settings["shuffle_answers"] = not self.settings["shuffle_answers"]
                            break
                        elif temp == "n":
                            break
                        else:
                            print(Fore.RED + Style.BRIGHT + "You msut input a [Y/N]!")
        else:
            if type(kwargs["scoring_correct"]) == int:
                self.settings["scoring"]["correct"] = kwargs["scoring_correct"]
            else:
                raise InvalidArgumentError("The value inputed through the argument is not valid")
        print("Shuffling system changed successufully!\n")

    def change_preview(self):
        if self.settings["preview"]:
            print(Fore.YELLOW + "Current \"Preview\": ON")
        else:
            print(Fore.YELLOW + "Current \"Preview\": OFF")
        while True:
            temp = input("Do you want to change it? [Y/N] ").lower()
            if temp == "y":
                self.settings["preview"] = not self.settings["preview"]
                break
            elif temp == "n":
                break
            else:
                print(Fore.RED + Style.BRIGHT + "You must input a [Y/N]!")

        print("Shuffling system changed successufully!\n")
    
    def add_question(self, number_options, question, *args, **kwargs):
        question_temp = {"question": question, "answers": []}
        for x in range(1, number_options + 1):
            option = input("Option " + ALPHA_ORDER[x] + ". ")
            question_temp["answers"].append({"option": option, "correct": False})
        while True:
            correct = input("\nWhat option is the correct one? Write the letter: ").upper()
            for x in enumerate(question_temp["answers"]):
                if REVERSE_ALPHA_ORDER[correct] == x[0] + 1:
                    question_temp["answers"][x[0]]["correct"] = True
                    break
                else:
                    question_temp["answers"][x[0]]["correct"] = False               
            else:
                print(Fore.RED + Style.BRIGHT + "You must input the letter of the correct option!")
                continue
            break
        self.questions.append(question_temp)
        print("Question added successufuly!\n")

    def delete_question(self, number):
        temp = self.questions.pop(number - 1)
        print(temp)
        print("Question deleted successufuly!\n")

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

        # Name
        self.name = input("What's the name of this quiz?\n")
        print("Setup successfull!\n")

    # Method for printing the quiz
    def __str__(self, **kwargs):
        super().__str__()
    
        print(Style.BRIGHT + "\nQUIZ QUESTIONS: ")
        
        if self.questions == []:
            print("There are currently no questions")
        else:
            counter_questions = 1
            for x in self.questions:
                counter_answers = 1
                print("\nQuestion {}: {}\n".format(counter_questions, x["question"]))
                for y in x["answers"]:
                    if y["correct"]:
                        print(Style.BRIGHT + Fore.GREEN + "Option {}: {}".format(ALPHA_ORDER[counter_answers], y["option"]))
                    else:
                        print("Option {}: {}".format(ALPHA_ORDER[counter_answers], y["option"]))
                    counter_answers += 1
                counter_questions += 1
        return ""

# Class used in QuizingPlayer.py
# DONE!
class QuizPlayMode(Quiz):
        
    def play(self):
        print("Let's play!")

        temp = copy.deepcopy(self.questions)
        score = 0
        got_right = 0

        if self.settings["shuffle_questions"]:
            random.shuffle(temp)
    
        if self.settings["shuffle_answers"]:
            for x in enumerate(temp):
                random.shuffle(temp[x[0]]["answers"])

        print(temp)
        print(self.questions)

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

    # Method for printing the quiz
    def __str__(self, **kwargs):
        super().__str__()
    
        print(Style.BRIGHT + "\nQUIZ QUESTIONS: ")
        
        if self.questions == []:
            print("There are currently no questions")
        else:
            counter_questions = 1
            for x in self.questions:
                counter_answers = 1
                print("\nQuestion {}: {}\n".format(counter_questions, x["question"]))
                for y in x["answers"]:
                    print("Option {}: {}".format(ALPHA_ORDER[counter_answers], y["option"]))
                    counter_answers += 1
                counter_questions += 1
        return ""

if __name__ == "__main__":
    input("Please use QuizingProject to start! Press Enter . . . ")
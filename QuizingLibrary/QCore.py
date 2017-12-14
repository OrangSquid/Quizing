# As the name suggets, this is the core of the quizing project
# It contains the classes and the methods to play and create the quizes

import string
import getpass
from __init__ import *

# This module is in a try/except statement to prevent errors from hapening 
# Since it doesn't belong to the standard library
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

# Dicitonary to quiz options
alpha_order = dict(enumerate(string.ascii_uppercase, 1))

# Base Class for the CreateMode and PlayMode
class Quiz():
    def __init__(self, name, questions, correct_answers):
        self.name = name
        self.questions = questions
        self.correct_answers = correct_answers
        self.CONST_version_number = "a0.1"

# Class Used in QuizMaker.py
class QuizCreateMode(Quiz):
    def __init__(self, name, questions, correct_answers, settings):
        super().__init__(name, questions, correct_answers)
        self.settings = settings

    # Methods for changing the settings of the quiz
    # Every method that starts with "change__" is about changing the settings of the quiz
    def change__number_options(self):
        print(Back.RED + Style.BRIGHT + "Please note that the current questions won't be affected!\n")
        try:
            self.settings["default options"] = int(input("How many options do you want then?"))
        except:
            print(Fore.RED + Style.BRIGHT + "You must input a number !!\n")
            self.change_settings.number_options()
        print("The default number of options was changed successfully!")

    def change__name(self):
        self.name = input("What's the new name of the quiz? The current name is {}\n\n".format(self.name))
        print("Name changed successfully!")

    def change__scoring(self, option):
        if option == "1":
            while True:
                print("Right now, for each wrong question you get {}.".format(self.settings["question points"][0]))
                try:
                    self.settings["question points"][0] = int(input("How many points should the player get?"))
                    break
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
                    continue
                print("Scoring system changed successufully!")
                return

        elif action == "2":
            while True:
                print("Right now, for each right question you get {}.".format(self.settings["question points"][1]))
                try:
                    self.settings["question points"][0] = int(input("How many points should the player get?"))
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
                    continue
                print("Scoring system changed successufully!")

    # Method for printing the quiz
    def __str__(self):
        print("These are the quiz settings\n")
        print("Default number question optitions: {}".format(self.settings["default options"]))
        print("Wrong Answer points: {}".format(self.settings["scoring"][0]))
        print("Right Answer points: {}".format(self.settings["scoring"][1]))
    
        if self.questions == {}:
            print("There are currently no questions")
        else:
            print("\nThese are the questions\n")
            number = 1
            for x in self.questions.values():
                for y in zip(x.keys(), x.values()):
                    if "question" in y[0]:
                        print("{} {} : {}".format(y[0], number, y[1]))
                    else:
                        if self.correct_answers[number - 1] in y[0]:
                            print(Fore.GREEN + "{}. {}".format(y[0], y[1]))
                        else:
                            print("{}. {}".format(y[0], y[1]))
                print("", end = "\n")
                number += 1
        return ""
    
    # Method for adding a question
    def add_question(self, number, question):
        question_temp = {"question": question}
        for x in range(1, number + 1):
            question_temp["Option " +  alpha_order[x]] = input("Option " + alpha_order[x] + ". ")
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
        self.questions["question " + str(len(self.questions) + 1)] = question_temp
        self.correct_answers.append(correct)

    # Method for deleting a question
    def delete_question(self, number):
        for x in self.questions:
            if str(number) in x:
                del x

    # Method for setting the settings
    def set_settings(self):
        try:
            self.settings["default options"] = int(input("How many options will be the default number?\n"))
            while self.settings["default options"] >= 26 or self.settings["default options"] <= 3:
                self.settings["default options"] = int(input("The number must be between 2 and 26! "))
            w = int(input("How many points should the player get for each wrong answer?\n"))
            r = int(input("How many points should the player get for each right answer?\n"))
        except:
            print(Fore.RED + Style.BRIGHT + "You must input a number!")
            self.set_settings()
        self.settings["scoring"] = [w, r]
        self.name = input("What's the name of this quiz?\n")
        print("Setup successfull!")

class QuizPlayMode(Quiz):
    def __init__(self, name, questions, correct_answers, settings):
        super().__init__(name, questions, correct_answers)
        self.scoring = settings["scoring"]
        # Variable to hold the number of points the player has got and
        # The number of questions the player got right
        self.points = 0
        self.right = 0
        
    def play(self):
        if self.quiz_ver == CONST_version_number

        print("Let's play!")
        number = 1
        for x in self.questions.values():
            for y in zip(x.keys(), x.values()):
                if "Question" in y[0]:
                    print ("{} {}: {}".format(y[0], number, y[1]))
                else:
                    print ("{}. {}".format(y[0], y[1]))
            answer = input("\nAnd your answer is: ").upper()
            print()

            if answer == self.correct_answers[number - 1]:
                for y in zip(x.keys(), x.values()):
                    if "Option" in y[0]:
                        if y[0][7] == answer:
                            print(Fore.GREEN + "{}. {}".format(y[0], y[1]))

                        else:
                            print("{}. {}".format(y[0], y[1]))

                print("\nYou're right! You get {} points\n".format(self.scoring[1]))
                self.points += self.scoring[1]
                self.right += 1

            else:
                for y in zip(x.keys(), x.values()):
                    if "Option" in y[0]:
                        if y[0][7] == answer:
                            print(Fore.RED + "{}. {}".format(y[0], y[1]))

                        elif y[0][7] == self.correct_answers[number - 1]:
                            print(Fore.GREEN + "{}. {}".format(y[0], y[1]))

                        else:
                            print ("{}. {}".format(y[0], y[1]))
                print("You're wrong! You get {} points\n".format(self.scoring[0]))
                self.points += self.scoring[0]
            number += 1
        print("You got {} answers right and {} points\n".format(self.right, self.points))

# Hello me from the future!
# I just wanted to tell you that this project took you a while to do
# And if you find it stupid, clutered or innefecient, you're free to change it
# I'm writting this on the 8th September, 2017, 13h48m and I still haven't finished it
# I hope you're having a great time and wish you the best of luck!

# UPDATE: Hi me from the past and the future, this code is a mess and right now I'm fixing it
# I won't fix everything (obviously), but probably the me from the future will fix it. Right now is 7th November 2017, 20h51

# * Why the fuck didn't you first commented this
# I have been staring at this for a whole 10 minutes
# Trying to figure it out
# Dumbass
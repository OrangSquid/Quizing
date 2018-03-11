import string
import getpass
import os
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

# Dicitonary to hold alphabet for quiz options
alpha_order = dict(enumerate(string.ascii_uppercase, 1))

class Quiz():
    def __init__(self, name, questions, correct_answers):
        self.name = name
        self.questions = questions
        self.correct_answers = correct_answers

# Class Used in QuizingEditor.py
class QuizCreateMode(Quiz):
    def __init__(self, name, settings, questions):
        super().__init__(name, questions)
        self.settings = settings

    def change_number_options(self):
        print(Back.RED + Style.BRIGHT + "Please note that the current questions won't be affected!\n")
        try:
            self.settings["default_options"] = int(input("How many options do you want then?"))
        except:
            print(Fore.RED + Style.BRIGHT + "You must input a number !!\n")
            self.change.number_options()
        print("The default number of options was changed successfully!")

    def change_name(self):
        self.name = input("What's the new name of the quiz? The current name is {}\n\n".format(self.name))
        print("Name changed successfully!")

    def change_scoring(self, option):
        if option == "1":
            while True:
                print("Right now, for each wrong question you get {}.".format(self.settings["scoring"]["incorrect"]))
                try:
                    self.settings["scoring"]["incorrect"] = int(input("How many points should the player get?"))
                    break
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
                    continue
            print("Scoring system changed successufully!")

        else:
            while True:
                print("Right now, for each right question you get {}.".format(self.settings["scoring"]["correct"]))
                try:
                    self.settings["scoring"]["correct"] = int(input("How many points should the player get?"))
                    break
                except:
                    print(Fore.RED + Style.BRIGHT + "You must input a number!")
                    continue
            print("Scoring system changed successufully!")

    def change_timer(self, time):
        self.settings["timer"] = time
        print("Timer changed successufully!")

    def change_shuffling(self, option):
        if option == "1":
            while True:
                if self.settings["shuffle_questions"]:
                    print("Right now, the shuffling for questions is on")
                else:
                    print("Right now, the shuffling for questions is off")
                temp = input("Do you want to change it[Y/N]? ").lower()
                while temp != "y" or temp != "n":
                    temp = input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
                if temp == "y":
                    self.settings["shuffle_questions"] == not self.settings["shuffle_questions"]
            print("Shuffling system changed successufully!")

        else:
            while True:
                if self.settings["shuffle_questions"]:
                    print("Right now, the shuffling for questions is on")
                else:
                    print("Right now, the shuffling for questions is off")
                temp = input("Do you want to change it[Y/N]? ").lower()
                while temp != "y" or temp != "n":
                    temp = input(Style.BRIGHT + Fore.RED + "You must input a [Y/N]! ")
                if temp == "y":
                    self.settings["shuffle_questions"] == not self.settings["shuffle_questions"]
            print("Shuffling system changed successufully!")

    # Method for printing the quiz
    def __str__(self):
        print("These are the quiz settings\n")
        print("Default number question optitions: {}".format(self.settings["default_options"]))
        print("Wrong Answer points: {}".format(self.settings["scoring"]["incorrect"]))
        print("Right Answer points: {}".format(self.settings["scoring"]["correct"]))
    
        if self.questions == {}:
            print("There are currently no questions")
        else:
            print("\nThese are the questions\n")
            number = 1
            for x in questions:
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
    
    def add_question(self, number, question):
        question_temp = {"Question": question}
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
        self.questions.append(question_temp)

    def delete_question(self, number):
        temp = self.questions.pop(number - 1)
        print(temp)

    def set_settings(self):
        # Default õptions number and scoring
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
class QuizPlayMode(Quiz):
    def __init__(self, name, settings, questions):
        super().__init__(name, questions)
        self.scoring = settings["scoring"]
        # Variables to hold the number of points the player has got and
        # The number of questions the player got right
        self.points = 0
        self.right = 0
        
    def play(self):
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

                print("\nYou're right! You get {} points\n".format(self.scoring["correct"]))
                self.points += self.scoring["correct"]
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
                print("You're wrong! You get {} points\n".format(self.scoring["incorrect"]))
                self.points += self.scoring["incorrect"]

            number += 1
        print(Style.BRIGHT + "END!")
        print("You got {} answers right and {} points\n".format(self.right, self.points))

if __name__ == "__main__":
    import sys
    input("Please use QuizingProject to start! Press Enter . . . ")
    sys.exit(0)

# * Why the fuck didn't you first commented this
# I have been staring at this for a whole 10 minutes
# Trying to figure it out
# Dumbass

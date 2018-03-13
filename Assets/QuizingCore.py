import string
import getpass
import os
from colorama import *

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

# Dicitonary to hold alphabet for quiz options
alpha_order = dict(enumerate(string.ascii_uppercase, 1))

class Quiz():
    def __init__(self, name, questions, settings):
        self.name = name
        self.questions = questions
        self.settings = settings

# Class Used in QuizingEditor.py
class QuizEditMode(Quiz):
    def __init__(self, name, questions, settings):
        super().__init__(name, questions, settings)

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
                    self.settings["shuffle_questions"] = not self.settings["shuffle_questions"]
            print("Shuffling system changed successufully!")

        else:
            while True:
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

    def print_question(self, question):
        pass

    # Method for printing the quiz
    def __str__(self):
        print("These are the quiz settings\n")
        print("Default number question optitions: {}".format(self.settings["default_options"]))
        print("Wrong Answer points: {}".format(self.settings["scoring"]["incorrect"]))
        print("Right Answer points: {}".format(self.settings["scoring"]["correct"]))
        print("Shuffling questions: {}".format(self.settings["shuffle_questions"]))
        print("Shuffling answers: {}".format(self.settings["shuffle_answers"]))
        print("Timer: {}".format(self.settings["timer"]))
    
        if self.questions == []:
            print("There are currently no questions")
        else:
            counter_question = 1
            counter_answers = 1
            for x in self.questions:
                print("\nQuestion {}: {}\n".format(counter_questions, x["question"]))
                for y in x["answers"]:
                    if y["correct"]:
                        print(Style.BRIGHT + Fore.GREEN + "Option {}: {}".format(alpha_order[counter_answers - 1], y["option"]))
                    else:
                        print("Option {}: {}".format(alpha_order[counter_answers - 1], y["option"]))
                    counter_answers += 1
                counter_questions += 1
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
    def __init__(self, name, questions, settings):
        super().__init__(name, questions, settings)
        
    def play(self):
        print("Let's play!")
        if shuffle_questions:
            pass
        else:
            counter_questions = 1
            counter_answers = 1
            for x in self.questions:
                print("Question {}: {}\n".format(counter, x["question"]))
                for y in x["answers"]:
                    print("Option {}: {}".format(counter_answers - 1, y["option"]))
                answer = input("\nAnd your answer is: ").upper()
                print()

                if x["answers"][alpha_order.index(answer)]["correct"]:
                    for y in x["answers"]:
                        if shit:
                            pass

                    print("\nYou're right! You get {} points\n".format(self.scoring["correct"]))
                    self.points += self.settings["scoring"]["correct"]
                    self.right += 1

                else:
                    for y in zip(x.keys(), x.values()):
                        if "Option" in y[0]:
                            if y[0][7] == answer:
                                print(Styele.BRIGHT + Fore.RED + "{}. {}".format(y[0], y[1]))

                            elif y[0][7] == self.correct_answers[number - 1]:
                                print(Style.BRIGHT + Fore.GREEN + "{}. {}".format(y[0], y[1]))

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

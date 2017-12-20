# Script to handle file opening and starting 
# (You need to get good at naming)

import os
import sys
import getpass
import json
import QuizingLibrary as QL

# This module is in a try/except statement to prevent errors from hapening 
# Since it doesn't belong to the standard library
try:
    from colorama import *
except ModuleNotFoundError as e:
	QuizingLibrary.install_modules()

print(Style.BRIGHT + "Welcome to the Quizing Project!\n")

def choose_path(*file):
	temp = None
	try:
		with open(file[0], "r") as f:
			temp = json.load(f)
	except:
		# This is out of order to make sure it matches with the
		# if statements below
		# (lazy bitch)
		file_exists = False
		print("\nWould you like to:\n")
		print("1. Make a Quiz")
		print("3. Exit")
	else:
		file_exists = True
		print("\nWould you like to:\n")
		print("1. Edit the Quiz")
		print("2. Play the Quiz")
		print("3. Exit")
		print()

	while True:
		print(temp)
		action = input()

		# Make or Edit Quiz
		if action == "1":
			if temp == None:
				name = input("What will be the name of the file? ")
				with open("{}.quiz".format(name), "w") as f:
					json.dump({}, f, sort_keys = True)
				with open("{}.quiz".format(name), "r") as f:
					temp = json.load(f)

			quiz = QL.QuizingCore.QuizCreateMode(temp)
			del temp
			QL.QuizingMaker.start_edit(quiz)

		# Play Quiz
		elif action == "2" and file_exists:
			quiz = QL.QuizingCore.QuizPlayMode(temp)
			del temp
			QL.QuizingPlayer.start_play(quiz)

		# Exit
		elif action == "3":
			getpass.getpass("Press Enter to exit . . .")
			sys.exit()

		else:
			print("You must input a valid number!")

# Checks if user has inputed a file through drag'n'drop
# or opened it directly
try:
	if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".quiz"):
		print("You have inputed a valid file!\n")
		choose_path(sys.argv[1])
	else:
		# This sentence will probably get out sometime, but I will leave
		# it here for debugging purpuses
		print("You haven't inputed a valid file through drag'n'drop!\n")
		getpass.getpass("Press Enter to exit . . . ")
		sys.exit()
except:
	print("You haven't inputed a file through drag'n'drop!")

# In case the user doesn't provide any file the script
# will search in the current directory
filenames = os.listdir(os.curdir)

valid_options = []

# Checks if file has a valid extension
for filename in filenames:
    if os.path.isfile(filename) and filename.endswith(".quiz"):
    	valid_options.append(filename)

if valid_options == []:
	print("There's no quiz file in the current directory")
	print("You can drag and drop the file into the program")
	print("or change it into this directory.\n")
	choose_path()
elif len(valid_options) == 1:
	print("You only have a quiz file in this directory")
	print(valid_options[0])
	choose_path(valid_options[0])
else:
	print("You have multiple quiz files")
	print("Please choose one!")
	option = 1
	for file in valid_options:
		print("{}. {}".format(option, file))
		option += 1
	while True:
		try:
			option = int(input())
		except:
			print("You must input a valid number!")
			continue
		if option <= len(valid_options):
			choose_path(valid_options[option - 1])
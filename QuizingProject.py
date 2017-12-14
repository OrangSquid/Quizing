# Script to handle file opening and starting 
# (You need to get good at naming)

import os
import sys
import getpass
import QuizingLibrary

print("Welcome to the Quizing Project!\n")

def choose_path(*file):
	try:
		file[0]
	except:
		file_exists = False
		print("Would you like to:\n")
		print("1. Make a Quiz")
		print("3. Exit")
	else:
		file_exists = True
		print("Would you like to:\n")
		print("1. Make a Quiz")
		print("2. Play a Quiz")
		print("3. Exit")
		print()

	while True:
		action = input()

		if action == "1":
			quiz = QuizingLibrary.QCore.QuizCreateMode(file)
			QuizingLibrary.QMaker.start(quiz)

		elif action == "2" and file_exists:
			quiz = QuizingLibrary.QCore.QuizPlayMode(file)
			QuizingLibrary.QPlayer.start(quiz)

		elif action == "3":
			getpass.getpass("Press Enter to exit . . .")
			sys.exit()

		else:
			print("You must input a valid number!")
			continue

# Checks if user has inputed a file through drag'n'drop
# or opened it directly
try:
	if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".quiz"):
		print("You have inputed a valid file!\n")
		choose_path(sys.argv[1])
	else:
		# This sentence will probably get out sometime, but I will leave
		# it here for debugging purpuses
		print("You haven't inputed a file though drag'n'drop!\n")
except:
	pass

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
	print("or change it into here\n")
elif len(valid_options) == 1:
	print("You only have a quiz file in this directory")
	print(valid_options[0])
else:
	print("You have multiple quiz files")
	print("Please choose one!")
	for file in valid_options:
		option = 1
		print("1. " + file)
		option += 1
	while True:
		try:
			option = int(input())
		except:
			print("You must input a valid number!")
			continue
		if option =< len(valid_options):
			choose_path(valid_options[option - 1])
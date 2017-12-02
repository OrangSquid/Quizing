# Script to handle file opening and starting (You need to get good at naming)

import os
import sys
import getpass

# These modules are in try/except statements to prevent errors from hapening 
# Since they don't belong to the standard library
try:
	import QuizMaker
except ModuleNotFoundError as e:
	print("\nAn error occured while importing QuizMaker.")
	print("Redownloading the program might be a possible solution.")
	print("\nError:", e)
	getpass.getpass("Press Enter to exit . . . ")
	sys.exit(-1)

try:
	import QuizPlayer
except ModuleNotFoundError as e:
	print("\nAn error occured while importing QuizPlayer.")
	print("Redownloading the program might be a possible solution.")
	print("\nError:", e)
	getpass.getpass("Press Enter to exit . . . ")
	sys.exit(-1)

filenames = os.listdir(os.curdir)

print("Welcome to the Quizing Project!\n")

valid_options = []

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

print("Would you like to:\n")
print("1. Make a Quiz")
print("2. Play a Quiz")

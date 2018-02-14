import os
import sys
import getpass
import json
import QuizingEditor as QE
import QuizingCore as QC
import QuizingPlayer as QP

# This module is in a try/except statement to prevent errors from hapening 
# Since it doesn't belong to the standard library
try:
	from colorama import *
except ModuleNotFoundError as e:
	print("Please wait while we install neccessary modules")
	os.system("pip install colorama")

# This is to make sure that when using colorama the color goes back into the original form
init(autoreset = True)

print(Style.BRIGHT + "Welcome to the Quizing Project!\n")

def main():

	def choose_path(*file):
		"""Diretcs the user to either QuizingEditor.py or QuzingPlayer.py"""
		try:
			with open(file[0], "r") as f:
				temp = json.load(f)
		except:
			# This is out of order to make sure it matches with the
			# if statements below
			# (lazy bitch)
			file_exists = False
			print("Would you like to:\n")
			print("1. Make a Quiz")
			print(Fore.RED + Style.BRIGHT + "3. Exit")
		else:
			file_exists = True
			print("Would you like to:\n")
			print("1. Edit the Quiz")
			print("2. Play the Quiz")
			print(Fore.RED + Style.BRIGHT + "3. Exit")
			print()

		while True:
			action = input()

			# Make or Edit Quiz
			if action == "1":
				if not file_exists:
					name = input("What will be the name of the file? ")
					with open("{}.quiz".format(name), "w") as f:
						json.dump(
							{"name" : name,
							"settings" : {},
							"questions" : {},
							"correct_answers" : []}, f, ident = "\t")
					with open("{}.quiz".format(name), "r") as f:
						temp = json.load(f)
					quiz = QC.QuizCreateMode(temp["name"], 
											 temp["settings"], 
											 temp["questions"], 
											 temp["correct_answers"])
					quiz.set_settings()
				else:
					quiz = QC.QuizCreateMode(temp["name"], 
											 temp["settings"], 
											 temp["questions"], 
											 temp["correct_answers"])
				QE.start_edit(quiz, file[0])
				sys.exit()

			# Play Quiz
			elif action == "2" and file_exists:
				quiz = QC.QuizPlayMode(temp["name"], 
									   temp["settings"], 
									   temp["questions"], 
									   temp["correct_answers"])
				QP.start_play(quiz)
				sys.exit()

			# Exit
			elif action == "3":
				getpass.getpass("Press Enter to exit . . .")
				sys.exit()

			else:
				print("You must input a valid number!")

	try:
		file = " ".join(sys.argv[1:])
		if os.path.isfile(file) and file.endswith(".quiz"):
			print("File detected through console argument\n")
			choose_path(file)
			sys.exit()
		else:
			print("Invalid file in console argument!\n")
			getpass.getpass("Press Enter to exit . . . ")
			sys.exit()
	except:
		# In case the user doesn't provide any file the script
		# will search in the current directory
		print(os.curdir)
		filenames = os.listdir(os.curdir)

		valid_options = []

		# Checks if file has a valid extension
		for filename in filenames:
			if os.path.isfile(filename) and filename.endswith(".quiz"):
				valid_options.append(filename)

		if valid_options == []:
			print("No file detected")
			choose_path()
		elif len(valid_options) == 1:
			print("File detected in current directory: ")
			print(valid_options[0])
			choose_path(valid_options[0])
		else:
			print("Multiple files detected in current directory")
			print("Please choose one!")
			option = 1
			for file in valid_options:
				print("{}. {}".format(option, file))
				option += 1
			while True:
				try:
					c_option = int(input())
				except:
					print("You must input a valid number!")
					continue
				if c_option <= len(valid_options):
					choose_path(valid_options[c_option - 1])

if __name__ == "__main__":
	main()

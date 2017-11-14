import QuizMaker.py
import QuizRuner.py
import os.path

filenames = os.listdir(os.curdir)

print("Welcome to the Quizing Project!\n")

valid_options = []

for filename in filenames:
    if os.path.isfile(filename) and filename.endswith(".quiz"):
    	valid_options.append(filename)
else:
	print("There's no quiz file in the current directory")
	print("You can drag and drop the file you want to play or change to here\n")
	print(valid_options)

print("Would you like to:\n")
print("1. Make a Quiz")
print("2. Play a Quiz")

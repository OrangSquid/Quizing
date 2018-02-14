# Quizing
Python script to make and play quizes.

## How it works
This script will search through the current directory for files with the .quiz extension and pass it it to either QuizingEditor.py or Quizing Player.py to edit or play the quiz, respectively. You can also pass the file you want through console arguments.

## The .quiz file
The .quiz file is pretty much a JSON file with a different extension. 
It has this format:
```json
{
	"name" : "Name of the quiz",
	"settings" : {
		"default_options" : "Default number of options for quick acess when editing quiz",
		"scoring" : ["Points scored when wrong", "Points scored when right"]
	},
	"questions" : {
		"1" : {
			"Question" : "How far is the Earth from the Sun?",
			"Option A" : "150.000.000km",
			"Option B" : "140.000.000km",
			"Option C" : "130.000.000km"
		},
		"2" : {
			"Question" : "Question Example",
			"Option A" : "Option Example",
			"..." : "..."
		}
	},
	"correct_answers" : ["A", "..."]
}
```

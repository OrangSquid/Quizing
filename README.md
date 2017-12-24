# Quizing
Python script to make and play quizes.

## How this works
This script will read through the current directory to files with the .quiz extension. If none are found it'll ask you to make one.
If you want you can also drag and drop into the programm.

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
			"Question" : "How far is Earth from the Sun?",
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

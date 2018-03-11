# Quizing
Python script to make and play quizes.

## How it works
This script will search through the current directory for files with the .quiz extension and pass it it to either QuizingEditor.py or Quizing Player.py to edit or play the quiz, respectively. You can also pass the file you want through console arguments (drag'n'drop or double click if script is associated with .quiz file).

## The .quiz file
The .quiz file is pretty much a JSON file with a different extension. 
It has this format:
```json
{
    "quiz ver": 1.0
    "name": "Name of quiz",
    "settings": {
        "default_options": 4,
        "scoring": {
            "incorrect": 0,
            "correct": 10
        },
        "shuffle_questions": false,
        "shuffle_answers": false,
        "timer": 0
    },
    "questions": [
        {
            "question": "How far is the Earth from the sun?",
            "answers": [
                {
                    "option": "150.000.000km",
                    "correct": true
                },
                {
                    "option": "140.000.000km",
                    "correct": false
                },
                {
                	"option": "130.000.000km",
                	"correct": false
                }
            ]
        },
        {
        	"question": "Question example?",
        	"answers": [
        		{
        			"option": "Example",
        			"correct": true
        		}
        	]
        }
    ]
}
```

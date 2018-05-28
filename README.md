# Quizing
Python script to make and play quizes.

## How it works
This script will search through the current directory for files with the .jquiz extension and pass it it to either QuizingEditor.py or Quizing Player.py to edit or play the quiz, respectively. You can also pass the file you want through console arguments (drag'n'drop or double click if script is associated with .jquiz file).

## The .jquiz file
The .quiz file is pretty much a JSON file with a different extension. 
It has this format:
```json
{
	"quiz ver": 1.0,
	"name": "Name of quiz",
	"settings": {
		"default_options": 4,
		"scoring": {
			"incorrect": 0,
			"correct": 10
		},
		"shuffle_questions": false,
		"shuffle_answers": false,
		"preview": false
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

## The .xquiz file
**NOTE**: The script still doesn't have support for this file
The .xquiz file XML file with a different extension. 
It has this format:
```xml
<quiz ver = 1.0>
	<name>sample1</name>
	<settings>
		<default_options number = 3/>
		<scoring>
			<incorrect number = -5/>
			<correct number = 10/>
		</scoring>
		<shuffle_questions on = false/>
		<shuffle_answers on = false/>
	<questions>
		<question>How far is Earth from the Sun?</question>
		<answers>
			<option correct = true>150.000.000km</option>
			<option correct = false>140.000.000km</option>
			<option correct = false>130.000.000km</option>
		</answers>
		<question>Question example</question>
		<answers>
			<option correct = true>Option example</option>
		</answers>
	</questions>
</quiz>
```

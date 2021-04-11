The explanation on the flow of the code is in the Final_Project.py

The app is pretty straightforward but the important part is that I'm using a trivia question generating API that pulls
the questions from the internet. I set this to be the default behavior so if it doesn't work (internet connection problems or antivirus maybe)
setting the USE_RANDOM_TRIVIA_GENERATOR = False at the beginning of the code should use the default questions (defined in questions.py in json string)

or alternatively, launching the app with True or False as an argument (not case sensitive) would set that value to one of those. Using anything else 
other than either of those will just use the default value

If you use the trivia generator, I'm dumping the json data into a file called "generatedquestions.json" so you can use that as a cheat-sheet to test the app
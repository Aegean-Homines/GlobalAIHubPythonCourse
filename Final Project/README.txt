General notes:

1. Same deal as HW3: detailed notes on top of the project file. I'll talk about what's cool down below though.
2. Similar to HW3, there's a field called USE_RANDOM_TRIVIA_GENERATOR and it's set to True by default (I'll explain it's use below)
You can either set that to False or use the cmd line argument to set that value to true or false (anything else and it'll remain as true)

NOW the use of that:

Entering 10 questions by hand every run is pain. Entering 10 questions by hand just once in a file and reading the file is less of a pain but still hurts
(I did do that btw - the "questions.py" file is just that: It has 10 default questions in Turkish in a single line json format)

At this point I think we've established two things about me: I'm lazy and what I want to get out of this course is to investigate what python has to offer. And at every step, python pleasantly
surprised me with what it has. One of those things is the ability to seamlessy send get commands and receive input from websites.

As a result, I looked up if there is any web services that provides online trivia that I can somehow get from the website and parse it in the app. And I found one!
It's called OpenTBD and it provides an API that generates a URL endpoint for us to use. Calling that URL returns us x number of questions in, you won't believe it, json format.
Since python also has a json library, it was pretty trivial to handle the flow. It returns 10 different random questions at every call, lists potential answers and actually does feel like
playing a game! Slap a UI on it and we actually have a pretty cheap online game.

However, if you don't feel comfortable with English trivia or using an internet service, you can choose to opt out of it and use some boring repetitive questions instead of an awesome test
of knowledge and wisdom. You call.

OH also, If you use the trivia generator, I'm dumping the json data into a file called "generatedquestions.json" so you can use that as a cheat-sheet to test the app
Have fun!
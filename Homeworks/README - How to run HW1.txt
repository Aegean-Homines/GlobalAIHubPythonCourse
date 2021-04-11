I created functions for each question
The main app is a function array. Takes input from the user then uses that as an index to run the question code block
If this is a bother then you can delete the main part and run each question code by calling "questionX()" for each question

ex: 
question1()
question2()
question2()

The input-taking works in a while loop so you can test it with different inputs for each question
type Exit (not case sensitive, I'm lower casing the input string) or Ctrl+C to quit the loop

NOTES:
1-) General notes are on top of the file
2-) The second question does work with more than single digit numbers (or negative numbers for that matter)
However, I did but a code block to test single digit-ness of the input, but it's commented out. Feel free to enable that part
if so desired (along with the negative value check)
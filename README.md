# CPSC-507-Exam-1

# Directions for submissions
Create a github repo called "Exam 1." Invite me as a collaborator to your repo. Download the repo files here as a zip file. Unzip the files and add them to your repo. Modify the files as appropriate according to the instructions. Do not change names. Commit and push changes to your repo.

# Directions for solutions
Do not change any of the code given to you (other than the comments which should absolutely be removed). I will run your code with the expected structure. Unless otherwise stated, you are welcome to add any additional lines of code or functions you find necessary. If you make changes in which your solutions do not run, you will receive no credit for that problem. All solutions should include a docstring description, including doctests. Unless otherwise specified, all functions should end with a return of the appropriate type and not a print statement.  Refrain from using AI or other online tools.  All solutions should be yours alone.  Failure to comply will be viewed as dishonesty and treated accordingly.  Feel free to reach out with any questions you may have.

# Problem 1
Reading and writing to standard input/output (from/to the terminal) can be managed by the sys library.  For example, if we wrote a .py file called name.py with the following content:

import sys \
name=input("What is your name?") \
print("Hello " + name + ", how are you today?") 

And then run the code in terminal with the command \
python name.py

It would prompt the user to respond with their name.  The input() function reads, line by line, the information given in standard in with an optional message displayed.  Once the user hits enter, whatever was typed would be bound to the variable name and the print statement with this value inserted would be written to the terminal.  

Modify this code to also read in the response to how are you?  If they respond with "good" (with any capitalization, punctuation, or extra spaces), your program should reply "I'm so glad!"  If they respond with "bad" (also with any capitalization, punctuations, or white spaces), your program should reply "I'm so sorry!".  For all other responses, your program should reply "[their response], huh?"  Your program should also write to a file called "welcome_letter.txt" in the current directory the content "It was so great to meet you today, [name]!"  For this file, make sure that the name is appropriately capitalized.

# Problem 2
Design a one-line function funct_applied_to_list which takes in a list and a function and returns a list with the function applied to each value of the list.  Without defining any other functions, use funct_applied_to_list to square all entries of a given list.  Leave this example in your solution file.

# Problem 3
Design a function is_sorted which takes in a list of numbers and returns True if they are in increasing or decreasing order and False otherwise.

# Problem 4
A palindrome is a string which is the same backwards and forwards, ignoring spaces, punctuation, and capitalization.  For example, "A man, a plan, a canal, Panama" is a palindrome.  Design a function is_palindrome which takes in a string and returns True if the string is a palindrome and False otherwise.

# Problem 5
The value of pi can be estimated using experimental data (like pseudo-randomly generated points).  But first, some math.  The area of a circle of radius 1 is pi.  If this circle is inscribed in a square (whose side length must then be 2) the probability that we land inside the circle is given by the ratio of the circle and square area: A_circle/A_square=pi/4.  To estimate pi, we can randomly generate points inside this square, find the ratio of those which fall inside the circle, and multiply that number by 4.

Imagine a square on the Cartesian plane with corners located at the (0,0), (2,0), (0,2), and (2,2) coordinates with an inscribed circle.  Design a function estimate_pi which takes a number n which represents the number of random points to generate, using np.random generates n points within the square, and returns the estimated value of pi.

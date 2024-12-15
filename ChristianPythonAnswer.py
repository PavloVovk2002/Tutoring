import random

###
#
# Pavlo Vovk
#
# Base Case: try, catch
# Case 1: A, S, M must contain upper and lower case
# Case 2: x >= 1; x <= 12
# Case 3: Number of questions limit?
# Case 4: user promt correct or incorrect
#
###

def math_practice():
# Ask the user for the type of math questions
# Ask the user how many questions they want to try
    operation = input("Enter A for addition, S for subtraction, M for multiplication: ").upper()
    num_questions = int(input("How many questions do you want to practice? "))
    
# Function to perform the math questions
    def ask_questions(operation, num_questions):
        for i in range(num_questions):
            rand1 = random.randint(1, 12)
            rand2 = random.randint(1, 12)

            if operation == 'A':
                correct_answer = rand1 + rand2
                user_answer = int(input(f"What is {rand1} + {rand2}? "))
            elif operation == 'S':
                correct_answer = rand1 - rand2
                user_answer = int(input(f"What is {rand1} - {rand2}? "))
            elif operation == 'M':
                correct_answer = rand1 * rand2
                user_answer = int(input(f"What is {rand1} * {rand2}? "))
            else:
                print("Invalid operation chosen.")
                return
            
# Check if the user's answer is correct
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.")
    
# Call the function with the user's choices
    ask_questions(operation, num_questions)

# Loop the program
while True:
    math_practice()
    play_again = input("Do you want to try more questions? (yes/no): ").lower()
    if play_again != 'yes':
        #print("Thank you for practicing! Goodbye!")
        break



###
#
# TakeAways
#
#
#
# Functions & Arguments
# 
# def my_function():
#   print("Hello from a function")
# my_function()
#
# def my_function(Argument1, Argument2):
#   print(fname + " Refrence text")
# 
# my_function("Chris")
# my_function("Jack")
# my_function("Argument1, 2, ect")
#
# While vs For loops
#
# While loop  : Is for conditions, such as "Print i as long as i is less than 6"
# For loop    : Is for iterations, such as "list of numbers 1-12, list of strings ["apple", "banana", "cherry"]"
#
# 
# Print(f)
#
# The f in the line of code indicates that the 
# string is an f-string (formatted string literal) 
# in Python. F-strings allow you to embed expressions 
# directly inside string literals, surrounded by curly 
# braces {}
#
#
# Conditions
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
#
#
# https://www.w3schools.com/python/default.asp
import random

def number1(num1, num2):
#operation = enter 1
  enter1 = input("Enter A for addition, S for subtraction, M for multiplication") 
  enter2 = int(input("How many questions do you want to practice?")) 
  question_count = 0
#Score count?
  score = 0

##############

#for loop vs while loop
while question_count < enter2:
  num1 = random.randint(1,12) 
  num2 = random.randint(1,12)

##############

#user answer should be the same 1, 2, 3
if enter1 == 'A':
  print (num1, "plus", num2, "=") 
  Correct_Answer = num1 + num2
elif enter1 == 'S':
  print (num1, "minus", num2, "=") 
  Correct_Answer = num1 - num2
elif enter1 == 'M':
  print (num1, "times", num2, "=") 
  Correct_Answer = num1 * num2
  user_answer = int(input("Your Answer = ")) 

##############

#return issue
if user_answer == Correct_Answer:
  print ("correct answer") 
  score += 1
else:
  print ("wrong")
  question_count = question_count +1 
  return score, enter2

def main():
  num1= random.randint(1,12) 
  num2= random.randint(1,12)
  result= number1(num1,num2) 
  print (result)

#Main for what?
#main()
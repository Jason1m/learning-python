# print("Hello, World!")
# print("Python is fun!")
# print("I am learning to code!")
# print("This is exciting")

#Printing Numbers

# print(15)
# print(47)
# print(6 + 4)
# print(20 + 30)
# print(58 - 25)
# print(8 * 8)

# my_name = "Tolu"
# my_age = 22

# print("This is a text")
# print(348)
# print("3673")

# name = input("What is your name? ")
# age = input("How old are you? ")

# print("Hello, " + name + "!")
# print("You are " + age + " years old")

# first_name = "Lara"
# last_name = "Jean"
# city = "New york"

# full_name = first_name +" "+ last_name

# print("Full name:", full_name)

# greeting = "Hello, " + full_name + "!"
# print(greeting)

# location_message = full_name + " lives in " + city
# print(location_message)

# print("\n---- Let's get to know you ----")
# user_name = input("What is your name? ")
# favorite_color = input("What is your favorite color? ")
# favorite_food = input("What is your favorite food? ")

#personalized message

#message = "Hello " + user_name + "! I  love that your favorite color is " + favorite_color + " and you like " + favorite_food + "!"
#print(message)

#Number variable
# score1 = 56
# score2 = 40
# score3 = 64

# total = score1 + score2 + score3
# average = total/3
# print("First score: ",score1)
# print("Second score: ",score2)
# print("Third score: ",score3)
# print("Total: ",total)
# print("Average: ",average)

#More examples

# birth_year = 2005
# current_year = 2025
# age = current_year - birth_year
#print("If you were born in ", birth_year, " you would be ", age , " years old in the year ", current_year)

#Converting text to number

# user_input = input("Enter a number: ")
# number = int(user_input)
# result = number * 2

# print("You entered:", user_input, "(as text)")
# print("You converted to number:", number)
# print("You times it by 2:", result)

#Python Basic Quiz
# print()
# print("Welcome to Python Basic Quiz")
# print("Let's see what you've learnt")
# print()

# #initialize score
# score = 0
# #Question 1
# print("Question 1: What function do we use to display text? ")
# answer1 = input("Your answer: ")

# if answer1.lower() == "print":
#     print("Correct!")
#     score = score + 1
# else:
#     print("The answer is 'print' - that's how we display text!")

#     print()

# #Question 2
# print("Question 2: What do we put around text in python?")
# answer2 = input("Your answer: ")

# if answer2.lower() == "quotes" or '"' or "'":
#     print("correct!")
#     score = score + 1
# else:
#     print("The answer is 'quotes'- we pur quotes around texts")

# print()

# #Question 3

# print("Question 3: What's 5 + 5 ? ")
# answer3 = input("Your answer: ")

# if answer3.lower() == "10":
#     print("correct!")
#     score = score + 1
# else: 
#     print("The answer is 10!")

# print()

# #Show final score

# print("Quiz complete!")
# print("Your score:", score , "out of 3")

# if score == 3:
#     print("Perfect!, you're ready for the next lesson")
# elif score == 2:
#     print("Good job!, Just review one concept and you'll be ready")
# else:
#     print("Good start! practice these concepts and try again")

# print("\n" + "=" * 50)
# print("CONGRATULATIONS! You've completed session 1")
# print("You now know the basics of talking to python")
# print("=" * 50)

# num1 = input("Enter your first number: ")
# num2 = input("Enter your second number: ")
# sum = num1 + num2

# print("num1 + num2 = ", num1 + num2)

#Simple questions with feedback


# question = "What is the capital of France?"
# print(question)
# user_answer = input("Your answer: ")
# if user_answer.lower() == "paris":
#     print("Correct! Well done!")
# else:
#     print("The answer is paris. Good try!")

#Multiple choices

# print("\nLet's try amultiple choice question: ")
# print("What language are we learning?")
# print("A) Django")
# print("B) JavaScript")
# print("C) Python")
# print("D) Spanish")
# choice = input("Enter your choice (A,B,C or D): ")
# if choice.upper() == "C":
#     print("Correct!, We're learning python.")
# else:
#     print("The answer is C - Python")

#Keeping Scores

# #Question 1
# score = 0
# print("\nQuestion 1: What symbol do we use for addition?")
# answer = input("Your answer: ")
# if answer == "+":
#     print("Correct!")
#     score = score + 1
# else:
#     print("The answer is +")

# #Question 2
# print("\nQuestion 2: What function is used to display text?")
# answer = input("Your answer: ")
# if answer == "print":
#     print("Correct!")
#     score = score + 1
# else:
#     print("The answer is print")

# #Show final answer
# print("\nYour final score: ", score, "out of 2")

#Adding personality and fun

#Step 1: Friendly Introduction
# print("Hello! i'm pybot, your friendly python assistant!")
# print("I'm here to help you learn programming!")

# name = input("What should i call you? ")
# print("Great to meet you", name, "!")

# #Step 2 : Personalized interaction
# print("\n" + name + ", I have a fun fact about your name ")
# print("Your name '"+ name +"' has " + str(len(name)) + " letters in it!")

# if len(name) <= 4:
#     print("Short and sweet! I like it!")
# elif len(name) <= 8:
#     print("That's a nice length for a name!")
# else:
#     print("Wow, that's a long name! Very distinguished!")

#Basic Quiz starts here

# print("\nWELCOME TO PYTHON BASIC QUIZ!")
# print("Let's see what you've learned!")
# print("=" * 40)

# #Get the student's name for personalization
# student_name = input("First what's your name: ")
# print("Hello," + student_name + "! Lets begin!")
# print()

# #Initialize scores to keep track of current answers

# score = 0
# total_questions = 3
# #Question 1
# print("Question 1:")
# print("What function do we use to display text on the screen?")
# answer1 = input("Your answer: ")

# if answer1.lower() == "print":
#     print("Correct! the print() function displays text!")
#     score = score + 1
# else:
#     print("Not quite. the answer is print - that's how we display text")
# print()
# #Question 2
# print("Question 2:")
# print("What do we put around text to tell python it's a string?")
# answer2 = input("Your answer: ")

# if answer2.lower() == "quotes" or answer2 == "'" or answer2 == '"':
#     print("Correct! We put quotes around strings!")
#     score = score + 1
# else:
#     print("Not quite. the answer is quotes - either single or double!")
# print()
# #Question 3
# print("Question 3:")
# print("What is 7 + 5 ?")
# answer3 = input("Your answer: ")

# if answer3.lower() == "12":
#     print("Correct! 7 + 5 = 12!")
#     score = score + 1
# else:
#     print("Not quite. 7 + 5 = 12")
# print()

# #Show final results with personalized feedback
# print("=" * 50)
# print("QUIZ COMPLETE!")
# print(student_name + "! your final score is: " + str(score) + " out of " + str(total_questions))

# #Give encouraging feedback based on score
# if score == total_questions:
#     print("Perfect score! You're a python super star!")
# elif score <= 2:
#     print("Great job! You're really getting a hang of it!")
# elif score <= 1:
#     print("Good start! Keep practising and you'll improve!")
# else:
#     print("Don't worry, everyone learns at their own pace. Try again!")
# print("Thanks for taking the quiz, " + student_name + "!")

#ENHANCED QUIZ WITH MORE FEATURES

# def enhanced_quiz():

#     print("Enhanced Python Basic Quiz")
#     print("This version has more questions and features")
#     print("=" * 50)

    #Get student information
# student_name = input("What's your name? ")
# grade = input("What grade are you in? ")

# print("Hello!," + student_name + " from " + grade + "!")
# print("Let's see how much you've learned from python!")
# print()

#     #initialize tracking variables

# score = 0
# total_questions = 5

# #Question 1: Print() function
# print("Question 1 of " + str(total_questions))
# print("What function display text on the screen? ")
# print("A) Display()")
# print("B) Print()")
# print("C) Show()")
# print("D) Output()")

# answer = input("Enter your choice(A, B, C or D): ")
# if answer.upper() == "B":
#     print("Excellent! print() is correct!")
#     score = score + 1
# else:
#     print("Wrong! The answer is B - print()")
# print()

# #Question 2: Variables
# print("Question 2 of " + str(total_questions))
# print("What symbol do we to store a value in a variable? ")
# print("Example: name ____ 'Alice'")

# answer = input("Your answer: ")
# if answer == "=":
#     print("Perfect! we use = to assign values to variables!")
#     score = score + 1
# else:
#     print("Wrong! The answer is = the equals sign ")
    
# print()

# #Question 3: String concatenation
# print("Question 3 of " + str(total_questions))
# print("How do we join two strings together? ")
# print("Example: 'Hello' ____ 'World'")

# answer = input("Your answer: ")
# if answer == "+":
#     print("Great! we use + to concatenate (join) strings together!")
#     score += 1
# else:
#     print("Wrong! The answer is + (the plus sign)")
    
# print()

# #Question 4: Interactive question about the student 
# print("Question 4 of " + str(total_questions))
# print("Let's practice with your information! ")
# birth_year = input("What year were you born?: ")

# #convert number and calculate age
# current_year = 2025
# age = current_year - int(birth_year)

# print("So you're about " + str(age) + " years old!")
# confirm = input("Is this correct? (Yes/No): ")

# if confirm.lower() == "yes" or confirm.lower() == "y":
#     print("Great! you understand how variables and maths work together!")
#     score += 1
# else:
#     print("That's okay - Calculating ages with variables takes practice!")
    
# print()

# #Question 5: Creative question

# print("Question 5 of " + str(total_questions))
# print("What's rhe best thing you learnt about python? ")
# print("There's no wrong answer, its about your opinion!")

# opinion = input("Your answer: ")

# print("That's a wonderful answer - '" + opinion + "'" )
# print("Everyone have their own reasons for loving python!")
# score += 1 #Everyone gets this point for participating.
# print()

# #Final result with detailed feedback
# print("=" * 50)
# print("QUIZ RESULT for " + student_name.lower() )
# print("=" * 50)

# print("Final score: " + str(score) + " out of " + str(total_questions))

# #Calculate percentage

# percentage = (score/total_questions) * 100
# print("Percentage : " + str(int(percentage)) + "%")

# #Detailed result

# if score == total_questions:
#     print("OUTSTANDING! Perfect score!")
#     print("You have mastered the basics of python!")
# elif score >= 4:
#     print("EXCELLENT! You're doing great!")
#     print("You understand most of the key concepts!")
# elif score >= 3:
#     print("GOOD JOB! You're on the right track!")
#     print("Review the concepts you missed and you'll be ready!")
# elif score >= 2:
#     print("KEEP GOING! You're learning!")
#     print("Practice these concepts and try again!")
# else:
#     print("GREAT START! Everyone begins somewhere!")
#     print("Don't give up - programming takes practice!")

# print("\nThanks for taking the enhanced quiz " + student_name)
# print("Keep coding and have fun with python")

#Password generator                           
# import random 
# import string
# print("Hello! we're creating a password generator today!")
# print("Let's get your information")
# user_name = input("Username: ")
# print("Generate your password")
# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range (length)) 
#     return password
# length = int(input("Enter the length of the password: "))
# print("Your random password is:", generate_password(length))

# for i in range(5):
#     print(i)
# for _ in range(5):
#     print("Hello")
# for x in "banana":
#     print(x)
fruits = ["Apple", "Banana", "Mango", "Pineapple", "Kiwi", "Carrot", "Orange"]
if "Apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

# fruits = ["Apple", "Banana", "Mango", "Pineapple", "Kiwi", "Carrot", "Orange"]
# fruits[1] = "Peach"
# print(fruits)

# fruits = ["Apple", "Banana", "Mango", "Pineapple", "Kiwi", "Carrot", "Orange"]
# fruits[1:3] = ["Black currant", "Blueberries"]
# print(fruits)

fruits = ["Apple", "Banana", "Mango"]
fruits[1:2] = ["Pineapple", "Orange"]
print(fruits)


    

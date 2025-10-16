#Assignment 1: Voter Eligibility
print(f"Welcome to Voters Eligibility Test")
name = input(f"Enter your name: ").strip()
print(f"Welcome {name}!, Let's check if you're eligible to vote.")
age = input (f"Enter your age: ").strip()
age = int(age)
if age >= 18:
    print(f"Congratulations {name}! You're eligible!")
else:
    print(f"Oops! You're not yet eligible to vote")

#Assignment 2: Numbers Comparisons
print("="* 50)
print(f"\nLet's compare numbers!")
num1 = int(input(f"Enter your first number: "))
num2 = int(input(f"Enter your Second number: "))

if num1 > num2:
   print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#Assignment 3: Checking for positive, negative or zero.

print(f"\nChecking for positive, negative or zero")
score = int(input(f"Enter number: "))
if score > 0:
    print(f"{score} is positive!")
elif score < 0:
    print(f"{score} is negative!")
else:
    print(f"{score} is zero!")

#Assignment 4: Checking for students score and grade
print(f"\nCheck for your grade down below")
score = int(input(f"Enter your score: "))
if score >= 70:
    print(f"Distinction!")
elif score in range (50, 70):
    print(f"Pass!")
else:
    print(f"Fail!")

#Assignment 5: Checking for even and odd numbers
print(f"Let's check for even and odd numbers!")
number = int(input(f"Enter number: "))
if number % 2 == 0:
    print(f"{number} is even number.")
else:
    print(f"{number} is odd number.")





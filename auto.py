#Simple list iteration
fruits = {"Orange", "Banana", "Apple", "Strawberry"}
print(f"Our fruit list = {fruits}")
for fruit in fruits:
    print(fruit)
#Another example with action
for fruit in fruits:
    print(f"I love eating {fruit}")

#The range function
print(f"The range() function creates a sequence of numbers")
print(f"range(5) gives: 0, 1, 2, 3, 4")
for numbers in range(5):
    print(numbers)
print(f"Other range patterns")
print(f"range(1, 6) gives: 1-5")
for i in range(1, 6):
    print(f"Numbers: {i}")
print(f"range(0,10,2) gives every 2nd number: ")
for i in range(0,10,2):
    print(f"Even:{i}")
print(f"range(10,0,-1) - countdown:")
for i in range(10,0,-1):
    print(f"Countdown:{i}")

#LOOP WITH CONDITIONS
print(f"\nLOOP WITH CONDITIONS")
print(f"You can combine loops with if statements for powerful automation!")
#Filter data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original number: {numbers}")

print("\nEven number only:")
for num in numbers:
    if num % 2 == 0:
        print(f"Even: {num}")

print("\nNumbers greater than 5")
for num in numbers:
    if num > 5:
        print(f"Big number: {num}")
    
    #For multiple conditions

print("\nNumbers that are even and greater than 5")
for num in numbers:
    if num % 2 == 0 and num > 5:
        print(f"Even and big number: {num}")

#Accumulating results
prices = [15.42, 43.22, 44.34, 52.35]
print(f"Prices: {prices}")

total = 0
for price in prices:
    total += price
    print(f"Adding ${price: .2f}, running total ${total: .2f}")
print(f"Final total: ${total: .2f}")

#Count specific items
words = ["apple", "mango", "avocado", "banana", "agbalumo"]
print(f"Words = {words}")

a_words = 0
for word in words:
    if word.startswith("a"):
        a_words += 1
        print(f"Found 'a' word : {word}")

print(f"Total words starting with 'a': {a_words}")

#another example
cars = ["Benz", "Lexus", "Toyota", "Acura", "Maserati", "Lorry", ""]
print(f"Cars: {cars}")

l_cars = 0
for car in cars:
   if car.startswith("L"):
    l_cars += 1
    print(f"Found cars that starts with 'L' : {car}")
print(f"Total number of cars starting with 'L' : {l_cars}")

#Collects results in a new list
print("\nCreating a new list with upper case words: ")
uppercase_words = []
for word in words:
    uppercase_word = word.upper()
    uppercase_words.append(uppercase_word)
    print(f"{word} > {uppercase_word}")

print(f"New list: {uppercase_words}")

#Processing real data

print("\n\n PROCESSING REAL DATA")

print("Let's process some realistic data!")
 #STUDENTS DATA
students_data = [
     {"name": "Alice", "grade": 89},
     {"name": "Bankole", "grade": 72},
     {"name": "Cole", "grade": 94},
     {"name": "Daphane", "grade": 98},
     {"name": "Emmanuel", "grade": 67}
 ]

print("\nStudent Grade Report")

total_score = 0
honor_students = []

for student in students_data:
    name = student ["name"]
    grade = student ["grade"]

    #Add total
    total_score += grade
    #Check for honor
    if grade >= 90:
        honor_students.append(name)
        status = "Honor Roll!"
    elif grade >= 80:
        status = "Good Standing"
    else:
        status = "Need Improvement"
    print(f"{name}: {grade}% {status}")




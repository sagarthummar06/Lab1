#Programming Concepts
# Variables and basic data types
name = "John"
age = 25
height = 1.75
is_student = True

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# Conditional statements
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Loops
for i in range(5):
    print("Iteration:", i)

while age < 30:
    age += 1
    print("Incremented age:", age)

# Lists and loops
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("Fruit:", fruit)

# Functions
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 5)
print("Sum:", result)

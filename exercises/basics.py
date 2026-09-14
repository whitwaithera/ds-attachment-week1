#variables&datatypes

name = "Your Name"
age = 22
height = 1.75
print(f"My name is {name}, I am {age} years old, and I am {height}m tall.")

#collection and loops
# list of 5 numbers.
# Loop through the list and print only the even numbers.
numbers = [10, 15, 22, 33, 40]
for num in numbers:
    if num % 2 == 0:
        print(f"Even number: {num}")

#functions
# # 1. Write a function that takes a list of numbers and returns the average.
def calculate_average(num_list):
    if len(num_list) == 0:
        return 0
    return sum(num_list) / len(num_list)

# Test the function
scores = [85, 90, 78, 92, 88]
print(f"Average score: {calculate_average(scores)}") 

#Error handling
# 1. Ask the user for a number and divide 100 by it.
# 2. Use try/except to handle if they enter 0 or a letter.
try:
    user_input = input("Enter a number to divide 100 by: ")
    number = float(user_input)
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: That was not a valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

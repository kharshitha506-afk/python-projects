# Simple Calculator in Python

# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b

# Main program
print("Simple Calculator")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take user input
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation
if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input! Please select 1, 2, 3, or 4.")

try:
    num = int(input("Enter a number:"))
    result = 10/num 
except (ZeroDivisionError,ValueError):
    print("Error:Division by zero or Invalid input")

def withdraw(amount):
    if amount < 0:
        raise ValueError("Invalid withdrawl amount - Amount cannot be negative")
    print(f"You have withdrawn ${amount}")

try:
    withdraw(-50)
except ValueError as e:
    print(e)

#Safe Calculator

#Step1:Define Calculator Functions
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y 

def multiple(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

#Step 2:Display Menu 
def show_menu():
    print("\n-----Safe Calculator Menu------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice(1-5): ")
    if choice == '5':
        print("Exiting the calculator. GoodBye!")
        break

    try:
        num1 = float(input("Enter  first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1,num2))
        elif choice == '2':
            print("Result", subtract(num1,num2))
        if choice == '3':
            print("Result:", multiple(num1,num2))
        elif choice == '4':
            print("Result", divide(num1,num2))
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invaliid input. Please enter a valid numbers.")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error ooccur {e}")

    
        
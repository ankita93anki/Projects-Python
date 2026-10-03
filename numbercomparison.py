#Number Comparison Tool

#Step 1: Get user input for two numbers
num1 = float(input("Enter the first numbers: "))
num2 = float(input("Enter the second numbers: "))

#Step 2:Compare the numbers
print("\n----Comparison Results----------")

if num1 == num2:
    print(f"Both numbers are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is less than {num2}")


#Step 3: Check if any number is zero
if num1 == 0 or num2 == 0:
    print("\n At least one number is zero.")
else:
    print("\n Both numbers are non-zero")
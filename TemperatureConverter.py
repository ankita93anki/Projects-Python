#Temperature Converter

#step 1: Dfine Conversion Function

def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32

def farenheit_to_celsius(farenheit):
    return (farenheit -32) *5/9

def celsisus_to_kelvin(celsius):
    return celsius + 273.15

def farenheit_to_kelvin(farenheit):
    return (farenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_farenheit(kelvin):
    return (kelvin - 273.15)* 9/5 + 32

#Step 2: Display the menu
def show_menu():
    print("\n------Temperature Converter Menu-----")
    print("1. Celsius to Farenheit & kelvin")
    print("2. Farenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4.Exit")

#Step 3: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice(1/2/3/4):")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius"))
        print(f"Farenheit: {celsius_to_farenheit}:.2f")
        print(f"Kalvin: {celsisus_to_kelvin}:.2f")

    if choice == '2':
        farenheit = float(input("Enter temperature in Farenheit"))
        print(f"Celsius: {farenheit_to_celsius}:.2f")
        print(f"Kelvin:{farenheit_to_kelvin}:.2f")

    if choice == '3':
        kelvin = float(input("Enter temperature in Kelvin"))
        print(f"Farenheit {kelvin_to_farenheit}:.2f")
        print(f"Celsius:{kelvin_to_celsius}:.2f")
    
    if choice == '4':
        print("You are exiting the Main Program loop")
        break

# Temperature Converter

#Step 1: Define conversion functions
def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32 

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5/9

def farenheit_to_kelvin(farenheit):
    return (farenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_farenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

#Step 2: Display the menu
def show_menu():
    print("\n Temperature Converter Menu:")
    print("1. Celsius to Farenheit & Kelvin")
    print("2. Farenheit tp Celsius & Kelvin")
    print("3. Kelvin to Celsius & Farenheit")
    print("4. Exit")

#step 3: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Farenheit: {celsius_to_farenheit(celsius)}")
        print(f"Kelvin: {celsius_to_kelvin(celsius)}")

    elif choice == '2':
        farenheit = float(input("Enter temperature in Farenheit:"))
        print(f"Celsius: {farenheit_to_celsius(farenheit)}")
        print(f"Kelvin: {farenheit_to_kelvin(farenheit)}")

    elif choice == '3':
        kelvin = float(input("Enter temperature in kelvin: "))
        print(f"Kelvin to Celsius: {kelvin_to_celsius(kelvin)}")
        print(f"kelvin to farenheit: {kelvin_to_farenheit(kelvin)} ")
    elif choice == '4':
        print("Existing the program, Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")

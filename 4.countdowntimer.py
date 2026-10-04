#Countdown Timer

import time

#Step 1: Get user input for contdown start
start = int(input("Enter the number to start the countdown from: "))

#Step 2: Countdown using a while loop
print("\n---- Contdown begins-------")
while start > 0:
    print(start)
    time.sleep(1)
    start -=1

#Step 3: Print final message
print("\n-----Contdown Complete!------")
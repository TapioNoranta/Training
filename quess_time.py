import time
import random

seconds = (random.randint(2, 10))

# Game begins

prompt = "In this game you need to quess how many seconds have past?"
prompt += "\nPress y when ready: "

while True:
   start = input(prompt)
   
   if start == 'y':
       print("\nStart counting...\n")
       break

# Start and stop the clock

time.sleep(seconds)

print("STOP!")

# Quess the time

while True:
    quess = input("Quess the time in seconds: ")
    quess = int(quess)

    if quess > seconds:
        print("Too high.")
    elif quess < seconds:
        print("Too low.")
    else:        
        print("You are correct. You won!")
        break


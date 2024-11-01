prompt = "\nPlease enter your age: "

while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
       print("You can enter free.")
    elif age < 12:
        print("The ticket is 10 euros.")
    else:
        print("The ticket is 15 euros.")
    break

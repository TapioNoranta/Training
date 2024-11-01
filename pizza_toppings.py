active = True
while active:
    topping = input("Please input a pizza topping: ")

    if topping == 'quit':
        break
    else:
        print(f"I've added {topping} to your pizza.")
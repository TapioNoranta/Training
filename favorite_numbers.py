favorite_numbers = {
    'john': 6,
    'jeff': 4,
    'christian': 2,
    'jack': 10,
    'penny': 7
    }

number = favorite_numbers['jeff']
print(f"Jeff's favorite number is {number}.")

number = favorite_numbers['john']
print(f"John's favorite number is {number}.")

number = favorite_numbers['christian']
print(f"Christian's favorite number is {number}.\n")

# Looping through the list

for name, number in favorite_numbers.items():
   print(f"Name: {name.title()}")
   print(f"Number: {number}\n")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# Loop through all values

print('\nLoop through all values:')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}")

# Looping through all keys

print('\nLoop through all keys:')

for name in favorite_languages.keys():
    print(name.title())

# Loop and stop to a friend

print('\nLoop and stop to a friend:')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

# Particular person

print('\nDid Erin take the poll:')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")

# Print all keys

print('\nPrint all keys:')
print(f"\n {favorite_languages.keys()}")

# Loop through keys in a particular order

print('\nLoop through in a particular order:')

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Loop through values

print('\nLoop through values:')

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Loop through values and use a set

print('\nLoop through values and use a set:')
for language in set(favorite_languages.values()):
    print(language.title())

# Loop to check the if person has taken the poll

print('\nLoop to check the if person has taken the poll:')

persons = {'jack', 'john', 'jeff', 'phil', 'edward'}

for person in persons:
    if person in favorite_languages.keys():
        print(f"Good job {person.title()} for taking the poll")
    else:
        print(f"{person.title()} please take the poll.")

# List of favorite languages

print('\nList of favorite languages:')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are {language}")
    for language in languages:
        print(f"\t{language.title()}")





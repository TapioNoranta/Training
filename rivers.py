rivers = {
    'nile': 'egypt',
    'thames': 'britain',
    'seine': 'france',
    }

# Print river and country in a sentence.

print("\nPrint river and country in a sentence:")

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

# Print name of each river

print("\nPrint name of each river:")

for river in rivers.keys():
    print(river.title())

# Print name of each country

print("\nPrint name of each country:")

for country in rivers.values():
    print(country.title())


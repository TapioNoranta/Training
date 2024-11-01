favorite_places = {
    'john': ['london'],
    'jack': ['new york', 'helsinki'],
    'sarah':['helsinki'],
 }

for name, cities in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for city in cities:
        print(f"\t{city.title()}")
cities = {
    'london' : {
        'country': 'united kingdom',
        'population': '9 million',
        'fact': 'Has the oldest subway in the world',
        },
    'helsinki' : {
        'country': 'finland',
        'population': '630 000 thousand',
        'fact': 'Over 300 islands within the city limits',
        },
    'new york': {
        'country': 'usa',
        'population': '8,3 million',
        'fact': 'Honking your horn is illegal.',
        }
    }

for city, information in cities.items():
    print(f"City: {city.title()}")
    country = information['country']
    population = information['population']
    fact = information['fact']
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}\n")
    

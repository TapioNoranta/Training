bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Element in a list

print(bicycles[0])
print(bicycles[1])

# Last Element

print(bicycles[-1])

# Using a value from list

message = f"My first bike was a {(bicycles[0])}"
print(message)

# Adding to a list

bicycles.append('tunturi')
print(bicycles)

# Remove last item from list

bicycles.pop()
print(bicycles)

# Sort the list

bicycles.sort()
print(bicycles)

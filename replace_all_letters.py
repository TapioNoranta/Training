word = 'Tiiiiifasdfasfiiiiiiiiiiiiii.'
word_length = 0

print(f"Word: {word}")
print(f"Word Length: {len(word)}")

while word_length < len(word):
  word_length += 1
  
  print(f"{'_'*word_length}{word[word_length:]}")
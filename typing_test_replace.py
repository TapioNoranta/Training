import keyboard
import time

word = 'This is Joonatan writing some text.'

print(word)
word_length = -1

while (word_length+1) < len(word):
  print(word_length)
  word_length += 1
  
  word = word.replace(word[word_length], "X")
  print(word)

for letter in word:
   print(letter)
   while True:
     keyboard.wait(letter)
     break
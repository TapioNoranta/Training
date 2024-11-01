import keyboard
import time

word = 'Wordwordwordwordword'
word_length = 0

for letter in word:
   while True:
      print(f"{' '*word_length}{word[word_length:]}")
      keyboard.wait(letter)
      word_length += 1
      break
#Function that will count number of unique English letters in a word


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  unique_letters_counter = 0
  for letter in letters:
    if letter in word:
      unique_letters_counter += 1
  return unique_letters_counter

print(unique_english_letters("Mississippi"))

print(unique_english_letters("colonel"))

print(unique_english_letters("parallel"))
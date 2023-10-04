import random

my_words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

selected_word = random.choice(my_words)
selected_word_list = list(selected_word)
random.shuffle(selected_word_list)
shuffled_word = ''.join(selected_word_list)

print("welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

print("Jumbled word:", shuffled_word)
user_input = input("Your guess: ")
if user_input != selected_word:
    print("Sorry, that's not correct. The word was:", selected_word)
else:
    print("Correct!")

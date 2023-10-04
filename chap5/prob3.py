import random

my_words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic','university')
selected_word = random.choice(my_words)
guessed_word = ["_"] * len(selected_word)
attempts = 6

print("Guess the word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")
print("Length of the selected word:", len(selected_word))

while attempts > 0 and "_" in guessed_word:
    print("Remaining attempts:", attempts)
    print("Current guessed word:", " ".join(guessed_word))
    
    guess = input("Guess a letter: ")
    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", selected_word)
else:
    print("Incorrect guess.")

if attempts == 0:
    print("You've used up all your attempts. the correct wored was",selected_word)

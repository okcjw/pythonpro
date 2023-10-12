import random

my_words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
selected_word = random.choice(my_words)
guessed_word = ["-"] * len(selected_word)
attempts = 6
guessed_letter = []

def display_hangman(incorrect_attempts):
    hangman = [
        '''
         -------
         |     |
         |
         |
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |
         |
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |     |
         |
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |    /|
         |
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |    /|\\
         |    
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |    /|\\
         |    / 
         |
         |
        -----------
        ''',
        '''
         -------
         |     |
         |     O
         |    /|\\
         |    / \\
         |
         |
        -----------
        '''
    ]
    return hangman[incorrect_attempts]

while attempts > 0 and "-" in guessed_word:
    print(display_hangman(6 - attempts))
    print("")
   
    print("You've used the following letters:")
    print(guessed_letter)
    print("")
    
    print("So far, the word is:\n", "".join(guessed_word))
    print("")

    guess = input("Enter your guess: ")
    
    guessed_letter.append(guess)

    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1

if "-" not in guessed_word:
    print("Congratulations! You guessed the word:", selected_word)
else:
    print("Incorrect guess.")

if attempts == 0:
    print("You've used up all your attempts. The correct word was", selected_word)


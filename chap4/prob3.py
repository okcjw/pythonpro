import random
number = random.randrange(1,101)
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible")
tries = 0

while True: 
    try:                     
        tries += 1
        guess = int(input("take a guess: "))
        if guess == number:
            print("You guessed it! the number was", number)
            break
        elif guess > number:
            print("Lower...")
        else:
            print("Upper...")
    except:                 
        print("Enter a number from 1 to 100")
        tries -= 1

print("And it only took you", tries, "tries!")

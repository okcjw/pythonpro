# Trivia Challenge Game
import random
import pickle

# Load the data file
file = open("trivia_data.pkl", "rb")
data = pickle.load(file)
file.close()

# Get the number of questions
num_questions = len(data)

# Choose a random question
index = random.randint(0, num_questions - 1)
question = data[index]

# Display the question and the choices
print("Welcome to Trivia Challenge!\n")
print(question["title"])
print(question["category"])
print(question["question"])
print()
for i in range(1, 5):
    print(f"{i} - {question['answer ' + str(i)]}")
print()

# Get the user's answer
answer = int(input("What's your answer? "))

# Check the answer and display the result
if answer == question["correct answer"]:
    print("That's correct!")
else:
    print("Sorry, that's wrong.")
print(question["explanation"])


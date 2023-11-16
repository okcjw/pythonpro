import random

def load_data(file_path):
    trivia_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i + 8 <= len(lines):
        trivia_item = {}
        title = lines[i].strip()
        category = lines[i + 2].strip()
        question = lines[i + 3].strip()
        answers = [lines[i + j].strip() for j in range(4, 8)]
        correct_answer = lines[i + 8].strip()
        explanation = lines[i + 9].strip()

        trivia_item['title'] = title
        trivia_item['category'] = category
        trivia_item['question'] = question
        trivia_item['answers'] = answers
        trivia_item['correct_answer'] = correct_answer
        trivia_item['explanation'] = explanation

        trivia_data.append(trivia_item)
        i += 11

    return trivia_data

def display_question(trivia_item):
    print('\tTitle: ' + trivia_item['title'])
    print('---------------------------------------')
    print('Category: ' + trivia_item['category'])
    print('Question: ' + trivia_item['question'])
    
    for i, answer in enumerate(trivia_item['answers'], 1):
        print(f"{i}. {answer}")

    print()

def get_user_answer():
    while True:
        try:
            answer = input('Enter your answer (1-4) or type "exit" to end the game: ')
            if answer.lower() == 'exit':
                return 'exit'
            answer = int(answer)
            if 1 <= answer <= 4:
                return answer
            else:
                print('Invalid input. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def check_answer(user_answer, correct_answer):
    return str(user_answer) == correct_answer

def main():
    file_path = 'trivia_data.txt'
    trivia_data = load_data(file_path)
    if not trivia_data:
        print("No trivia data found. Please check your file.")
        return
    
    while True:
        print()
        random_question = random.choice(trivia_data)

        display_question(random_question)
        user_answer = get_user_answer()

        if user_answer == 'exit':
            print('Exiting the game. Goodbye!')
            exit()
    
        if check_answer(user_answer, random_question['correct_answer']):
            print('Correct! the answer number is ' + random_question['correct_answer'] + '\n' + random_question['explanation'])
        else:
            print('Incorrect! the answer number is ' + random_question['correct_answer'] + '\n' + random_question['explanation'])
        
if __name__ == "__main__":
    main()


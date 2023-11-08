text_file = open("text3.txt", "w")
print("Input your string...")
while True:
    user_input = input(">> ")
    if user_input == 'Q':
        print("Write process has been finished")
        break
    text_file.write(user_input + "\n")
text_file.close()

text_file = open("text3.txt", "r")
print("\nYour inputs are below...")
contents = text_file.read()
print(contents)
text_file.close()


text_file = open('text_file.txt', 'r')

print("Opening and closing the file.\n")

print("Reading characters from the file.")
print(text_file.read(1))
print(text_file.read(5))
print("")

text_file.seek(0)
contents = text_file.read()
print("Reading the entire file at once.\n" + contents)

text_file.seek(0)
print("Reading characters from a line.")
print(text_file.readline(1))
print(text_file.readline(5))
print("")

text_file.seek(0)
line = text_file.readline()
print("Reading one line at a time.\n" + line)

text_file.seek(0)
print("Reading the entire file into a list.")
lines = text_file.readlines()
print(lines)
print(len(lines))

for line in lines:
    print(line, end="\n")

text_file.seek(0)
print("Looping through the file, line by line.")
for line in text_file:
    print(line, end="\n")

print("")

text_file.close()

input("Press the enter key to exit.")

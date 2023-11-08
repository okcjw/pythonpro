print("Opening and closing the file.")
text = open("text.txt", "r")

print("\nReading characters from the file.")
print(text.read(1))
print(text.read(5))

print("\nReading the entire File at once.")
text.seek(0)
whole = text.read()
print(whole)

print("\nReading characters from a line.")
text.seek(0)
print(text.readline(1))
print(text.readline(5))

print("\nReading one line at a time.")
text.seek(0)
print(text.readline())
print(text.readline())
print(text.readline())

print("\nReading the entire file into a list.")
text.seek(0)
lines = text.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)

print("\nLooping through the file. line by line.")
text.seek(0)
for line in text:
    print(line)

text.close()

input("Press the enter key to exit.")

print("Creating a text file with the write<> method.\n")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("And that would make this the third line.")
text_file.close()

print("Reading the newly created file.")
text_file = open("write_it.txt", "r")
contents1 = text_file.read()
print(contents1)
text_file.close()

print("\nCreating a text file with the writelines<> method.\n")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3"]
text_file.writelines(lines)
text_file.close()

print("Reading the newly created file.")
text_file = open("write_it.txt", "r")
contents2 = text_file.read()
print(contents2)
print("")
text_file.close()

input("Press the enter key to exit.")

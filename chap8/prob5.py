try:
    num = float(input("Enter a number: "))
except:
    print ("Something went wrong!")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print ("That was not a number!\n")
for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "-->", end="")
        print (float(value))
    except(TypeError, ValueError):
        print ("Something went wrong!")
print("")
for value in (None, "Hi!"):
   try:
       print ("Attempting to convert", value, "-->", end="")
       print (float(value))
   except(TypeError):
       print ("Can only convert string or number!")
   except(ValueError):
       print ("Can only convert a string of digits!")

try:
  num = float(input("\nEnter a number: "))
except(ValueError) as e:
  print ("That was not a number! Or as Python would say:\n", e)

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print ("That was not a number!")
else:
    print ("You entered the number", num)

input("\nPress the enter key to exit.")

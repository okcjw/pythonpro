import pickle
import shelve

print("Pickling lists.")

variety = ["sweet", "hot", "dill"]
pickle_file = open("pickles1.dat", "wb")  
pickle.dump(variety, pickle_file)
pickle_file.close()

variety = ["whole", "spear", "chip"]
pickle_file = open("pickles2.dat", "wb")  
pickle.dump(variety, pickle_file)
pickle_file.close()

variety = ["Claussen", "Heinz", "Ūlassic"]
pickle_file = open("pickles3.dat", "wb")  
pickle.dump(variety, pickle_file)
pickle_file.close()

print("\nUnpickling lists.")
pickle_file = open("pickles1.dat", "rb")  
variety = pickle.load(pickle_file)
print(variety)
pickle_file.close()

pickle_file = open("pickles2.dat", "rb") 
variety = pickle.load(pickle_file)
print(variety)
pickle_file.close()

pickle_file = open("pickles3.dat", "rb") 
variety = pickle.load(pickle_file)
print(variety)
pickle_file.close()

print("\nShelving lists.")

shelf_file = shelve.open("shelf_data")

shelf_file["variety"] = ["sweet", "hot", "dill"]
shelf_file["shape"] = ["whole", "spear", "chip"]
shelf_file["brand"] = ["Claussen", "Heinz", "Ūlassic"]
shelf_file.close()

print("\nRetrieving the lists from a shelved file:")
shelf_file = shelve.open("shelf_data")
for key in shelf_file.keys():
    print(key, "-", shelf_file[key])
shelf_file.close()

print("")
input("Press the enter key to exit.")


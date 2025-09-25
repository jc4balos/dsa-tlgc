grades = {"Kevin": 75, "Mia":74, "Rivera": 73}

print(grades.get("Mia")) #accessing values
print(grades.items()) #returns a tuple of key value pairs
print(grades.keys()) #prints all keys
print(grades.values()) #prints all values
print(grades.update({"Danilo": 99}))
print(grades)
grades["Kevin"] = 89 #changes the value for specific key
print(grades)
grades["Arjones"] = 62
print(grades)
grades.pop("Kevin") #Removes kevin
print(grades)
grades.popitem() # Removes the last item
print(grades)
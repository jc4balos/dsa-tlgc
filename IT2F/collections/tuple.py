cars = ("bmw", "ferrari", "Motolola", "Motolola")
print(cars[0])

# cars[0] = "toyota" (It doesn't work)
listcar = list(cars) #converted to list
listcar.append("Mitsubishi") #add new item as a list

print(listcar)

# for car in cars:
#     print(car)
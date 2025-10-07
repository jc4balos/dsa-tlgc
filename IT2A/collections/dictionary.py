grades = {"John Mark": 75,"Joren": 74,"Christian":65}
print(grades)
#delete items in dictionary
grades.pop("Joren")
print(grades)
grades.popitem()
print(grades)


#add item in dictionary
grades["Kishan"] = 35
print(grades)
grades.update({"Ralph": 100})
print(grades)

#Change items in dictionary
grades["Christian"] = 70
print(grades)
grades.update({"Joren":90})
print(grades)


#accessing items in dictionary
print(grades.get("John Mark"))
print(grades["Joren"])

#copy a dictionary
x = grades.copy()
print(x)


#remove all elements in dictionary
grades.clear()
print(grades)
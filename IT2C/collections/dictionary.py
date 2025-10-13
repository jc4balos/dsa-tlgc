grades ={"Jonas":75,"Jonel":90,"Laric":74}
print(grades)

#remove item
grades.pop("Laric")
print(grades.popitem())

#Add item
grades["Banay"] = 90
print(grades)

#change value in dict
grades.update({"Laric": 60})
print(grades)

grades["Jonel"] = 55
print(grades)

#access via index
print(grades["Jonel"])

#Access a value in dictionary
print(grades.get("Jonas"))
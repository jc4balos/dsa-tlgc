colors = {"red", "green", "blue"}
print(colors)

#remove item on set
colors.remove("red")
print(colors)

#add new item to set
colors.add("black")
colors.add("black")
print(colors)

#Access items in a set
for color in colors:
    print(color)

# get the length of a set
print(len(colors))
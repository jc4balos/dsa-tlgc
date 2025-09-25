colors = {"red", "green", "blue", "pink", "red"}
no_of_items = len(colors)
print(no_of_items)

#add item
colors.add("indigo")

#add duplicated item
colors.add("red")
colors.add("red")
colors.add("red")

#printing the set
for color in colors:
    print(color)

colors.add("violet")
print(colors)
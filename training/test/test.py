# Part 3
fruits = ["apple", "banana", "mango", "apple"]
fruits.remove("banana")
fruits.append("grape")
fruits.insert(0,"orange")

unique_fruits = set(fruits)
unique_fruits.add("melon")

fruit_prices = (("apple", 25, "red"), ("mango", 30, "orange"), ("grape", 20, "purple"))

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "orange",
    "grape": "purple"
}
fruit_colors["apple"] = "green"

print(fruits[0])
#1. What fruit is printed in line 20?


print(len(fruits))
#2. What is the output of line 24?


print(unique_fruits)
#3. How many items are printed in line 28?


print(fruit_prices[1][0])
#4. What is the output of line 32?


print(fruit_colors["apple"])
#5. What is the output of line 36?


#6. What is the data type of fruit_prices[0]?

print(fruit_colors.get("grape"))
#7. What is the output of line 42?


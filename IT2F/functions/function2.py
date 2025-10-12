def average(list):
    return sum(list)/ len(list)

def input_number():
    value = []
    for i in range(5):
        num=float(input(f"Enter Number{i + 1}:"))
        value.append(num)
    return value

print(average(input_number()))

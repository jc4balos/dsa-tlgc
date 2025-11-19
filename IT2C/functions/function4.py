# Create a function that
# will show if the parameter is
# Odd or Even

# x= 3%2
# print(x)

def isOddEven(num):
    result = num % 2
    if result == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
        
isOddEven(10)

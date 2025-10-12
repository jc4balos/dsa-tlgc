
# def add(num1,num2):
#     x = num1+num2
#     print(x)

# def subtract(num1,num2):
#     x = num1-num2
#     print(x)

# subtract(6,5)
    

def loop(n):
    i = 1
    while i <= n:
        print(i)
        i+=1

loop(7)

def quadratic_loop(n):
    i = 1
    while i <= n:
        j = 1
        while j <=n:
            print("Inner Loop: ", j)
            j+=1
        print("Outer Loop", i)
        i+=1


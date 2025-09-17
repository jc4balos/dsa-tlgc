def solve(x):
    result = (3*x)+1
    return result

print(solve(1000))

def bark():
    print("Arf Arf")

def say(name,age):
    print("My name is ", name, ". I am ", age, " years old.")

def output(n):
    i = 1
    while i <= n:# 6<=5 = FALSE
        j = 1
        while  j <=n:
            print("Loop inside")
            j+=1
        print("Loop Outside")
        i+=1

output(3)



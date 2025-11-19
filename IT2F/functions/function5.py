# Iteration

names = ["Charles", "Flicher", "Mia"]
# for name in names:
#     print(name)

i=0

def sum(a,b):
    return a+b

print(len(names))
while(i < len(names)):
    print(names[i])
    i+=1
    #i = i+ 1


# Recursion

def countdown(n):
    if n == 0:
        print("Countdown Stoppped! Happy New Year Ebriwan")
    else:
        print(n)
        
        


countdown(5)
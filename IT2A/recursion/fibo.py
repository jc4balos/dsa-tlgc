def fibo(n):
    if n == 0:
        return 0 # Base case
    elif n ==1:
        return 1 # Base case
    else:
        return fibo(n-1)+fibo(n-2)

x = 10
i = 0
while (i <= x):
    print(fibo(i))
    i+=1

# 0,1,1,2,3
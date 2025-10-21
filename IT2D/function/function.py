def fibo(n):
    list = [1,1]
    i = 0
    while(i < n-2):
        result = list[i]+list[i+1]
        list.append(result)
        i+=1
    print(list)

fibo(1)
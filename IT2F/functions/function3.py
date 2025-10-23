def fibo(n):
    list= [0,1]
    i=0
    while i<n:
        result = list[i]+ list[i+1]
        list.append(result)
        i+=1
    return list

print(fibo(10))



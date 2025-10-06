def nested_loop(n):
    i = 0
    print(i)
    while i <n:
        j = 0
        while j < n:
            print(j)
            j+=1
        i+=1

nested_loop(1000000)

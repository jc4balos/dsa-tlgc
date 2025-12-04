from collections import deque

queue = deque()

queue.append("Item 1")
queue.append("Item 2")
queue.append("Item 3")

print(queue[0])
print(len(queue))


if len(queue) == 0:
    print("EMPTY")
else: 
    print("Not Empty: ", queue)


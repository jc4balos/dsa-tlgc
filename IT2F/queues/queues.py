from collections import deque
queue = deque()

#Enque (add)
queue.append("gemson")
queue.append("Pogi")
queue.append("gemcyqtttttttt")

print(queue.popleft())
print(queue.popleft())

print(queue[0])

if len(queue) == 0:
    print("Empty")
else:
    print(queue)
    print("May laman")

print(len(queue))
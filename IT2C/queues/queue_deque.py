from collections import deque

queue = deque()

#Enqueue
queue.append("Ronnel")
queue.append("Vien")
queue.append("Lesley")

#Dequeue
queue.popleft()
print(queue)

#Peek
print(queue[0])

#Size
print(len(queue))


#isEmpty
def isEmpty(collection):
    if len(collection)==0:
        return True
    else:
        return False
    
print(isEmpty(queue))
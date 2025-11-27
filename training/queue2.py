from queue import Queue

names= Queue()

names.put("queue")
names.put("queue2")

print(names.get())
print(names.get())


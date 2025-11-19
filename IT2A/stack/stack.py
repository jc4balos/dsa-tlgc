# push
names = ["Jhorel", "John Mark", "Aubrey"]
names.append("Maria")

print(names)

#pop
print(names.pop())
print(names)

#peek
print(names[-1])

#size
print(len(names))

#isEmpty
names.pop()
names.pop()
names.pop()
if len(names) == 0:
    print("Empty")
else:
    print("Not Empty!")

print(len(names))
names = ["Daniel", "James", "Kz"]
#push
names.append("Patrick")
print(names)

#pop
print(names.pop())
print(names)

#peek
print(names[-1])

#isEmpty
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
print(names)
# names.pop()
# names.pop()
# names.pop()
print(isEmpty(names))

#size
print(len(names))
names = ["Tanggol", "Onyok", "Ronel"]

#push
names.append("CJ")
print(names)

#pop
print(names.pop())
print(names)
names.pop()
print(names)

#peek
print(names[-1])


#isEmpty
def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

# names.pop()
# names.pop()
print(isEmpty(names))

#size
print(len(names))
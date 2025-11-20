names = ["Johnny Sins", "Bentong", "Jollibee"]

#Push
names.append("Mcdo")
print("Pushed stack: ", names)

#Pop
print(names.pop())
print(names)

#Peek
print(names[-1])

#isEmpty
def isEmpty(collection):
    if len(collection) == 0:
        return False
    else:
        return True
    
print(isEmpty(names))

#Size
print(len(names))
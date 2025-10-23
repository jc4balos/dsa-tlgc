"""
Create a function that will store the
parameter in an existing list
call the function
then print the list
"""
names = [] # created an empty list
def add_to_list(name): # Created a function called add_to_list with parameter called name
    names.append(name) # add an item to a list

add_to_list("Pedro") # called the function
print(names) # print the list names
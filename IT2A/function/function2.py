# def sum(x,y):
#     result = x+y
#     return result

# print(sum(2,2))

#check username and password
username = "jcabalos"
password = "P@ssw0rd"

def check_credentials(input_username,input_password):
    if input_username == username and input_password == password:
        print("Welcome!!!")
    else:
        print("Access Denied")

check_credentials("jcabalos","P@ssw0rd")

"""
create a function that will return
if the credentials are correct or not
"""


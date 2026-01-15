def greet_user(name):
    message = "Hello,"+name+"!"
    return message

#main code 

user_name=input("Enter your name: ")
greeeting=greet_user(user_name)
print(greeeting)
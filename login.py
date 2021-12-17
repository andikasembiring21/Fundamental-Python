print("Create your Account")
username=input("input usernama: ")
password=input("input password: ")

if username != "":
    print(f"user '{username}' created succesfully")
    
print("Login now")
loguser=input("input username : ")
logpass=input("input password : ")

if (loguser == username) & (logpass == password):
    print("user logged in succesfully")
else:
    print("wrong!! correct again username or password")
    

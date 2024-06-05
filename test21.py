# username = "Min Khant Maung"
# password = "851995"

# username1 = input ("Enter your username: ")
# password1 = input ("Enter your password: ")

# if username == username1 and password == password1:
#     print("Hello user")
# else: 
#     print("invalid user")

username = "Min Khant Maung"
password = "851995"

username1 = input ("Enter your username: ")
password1 = input ("Enter your password: ")

if username == username1 and password == password1:
    print("Hello user")
elif username != username1 and password == password1:
    print("Worng username")
elif username == username1 and password != password1:
    print("Worng password")
elif username != username1 and password != password1:
    print("Invalid user")
else:
    print("System Error")
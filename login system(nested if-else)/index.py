#login system using nested if-else
username=input("Enter name=")
password=input("Enter password=")
if username=="saboor":
    if password == "hello world":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("usename incorrect")

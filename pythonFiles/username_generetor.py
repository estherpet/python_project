def username(email: str):
    username = ""
    for i in email:
        if i != "@":
            username += i
        else:
            break
    return username


names = input("Enter your email :")
emaiiil = "esther2331@gmail.com"
print(username(names))
print(username(emaiiil))

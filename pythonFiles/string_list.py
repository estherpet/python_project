name_list = []
for name in range(1, 6):
    name = input("Enter your name :")
    if len(name)  > 0 and len(name) <= 10:
        name_list.append(name)

    print(name_list)



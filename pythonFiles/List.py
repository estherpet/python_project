name = [["silver", 500, 10, 5000, "08120232456"], [
    "diamond", 1000, 20, 20_000, "08190496788"],
        ["Mary", 200, 10, 2000, "07055533316"],
        ["Lydia", 100, 10, 1000, "09160553536"],
        ["John", 600, 10, 6000, "08160555555"]]
for index, name in enumerate(name):
    print(index, name)

i, *others, b = name

print(name[4])
# print(i,others,b)

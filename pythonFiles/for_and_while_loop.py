name = "Ebube"
print(name[:: -1].title())

name = "Ebube"
print(name[:: - 1])

name = "Madam"
print(name[::-1].title())

name = "Anna"
print(name[:: -1].title())

num = (eval("1 + 6"))
print(num)
num = (2, 3)
print(pow(2, 3))
print(2 ** 3)

print(abs(-20))

print(round(3.6853, 2))

f_number = 2.36858
print(f"this number{f_number:,.3%}")
print(f"this number{f_number:,.2f}")

number = 3 ** .125
print(round(number, 3))
currency = 150000
print(f"{currency:,.2f}")

num = 2 / 10
print(f"{num:.0%}")

# while(True):
#     print("your name")


counter = 0
while (counter < 10):
    print("queenie", end=" ")
    counter = counter + 1

print(counter)

counter = 0
while (counter < 10):
    print("queenie")
    counter = counter + 1

print(counter)

for letter in "queenie":
    print(letter)

for i in range(5, 10):
    print(i)

for i in range(10):
    print(i)

for i in range(0, 11, 2):
    print(i)

for i in range(7):
    print("step")
    for e in range(3):
        print("clap")
        print()

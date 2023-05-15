number = list(range(1, 21))

print(number)

odd_number = number[::2]

print(odd_number)

number[4:10] = [0] * len(number[5:10])

print(number)

print(number[:7])

number[:] = []
print(number)



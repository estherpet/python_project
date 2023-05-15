# number = 1, 2, 3
# letter = "a", "b", "c", "d"
# print(number + letter)
# print(letter[:3])

number = tuple(range(1, 501))
print(number)
odd_number = number[::2]
print(odd_number)
even_number = number[1::2]
print(even_number)
add = even_number + odd_number
print(add)
x, y, z, *others = number
print(x, y, z, others)

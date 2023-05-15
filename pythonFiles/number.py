numbers = [1,2,3,4,5]
# numbers[0] = 10
# numbers [4] = 5055
# print(numbers)
# x,y, *others, = numbers
# print(x,y,others)
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# d = numbers[3]
# e = numbers[4]
a, *others, e = numbers
print(a,others,e)

letters = list("Hello C16")
print(letters)

for index, letters in enumerate(letters):
    print(index, letters)


# letters.append("e")
# letters.insert(0,"z")
print(letters)
set1 = {3, 4, 1, 2, 3, 3, 3}
print(set1)
num = {23, 45, 55, 66, 88, 4}
print(num | set1)
print(num - set1)
print(num & set1)
print(num ^ set1)
set1.add(10)
print(set1)
if 2 in set1:
    print("yes")

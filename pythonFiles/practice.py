number = 11211
first_number = number % 10
print(first_number)
number = number // 10
secondNumber = number % 10
print(secondNumber)
number = number // 10
third_number = number % 10
print(third_number)
number = number // 10
fourth_number = number % 10
print(fourth_number)
number = number // 10
fifth_number = number % 10
print(fifth_number)
total = first_number + secondNumber + third_number + fourth_number + fifth_number
print(total)
if first_number == fifth_number & secondNumber == fourth_number:
    print("it is a palindrome")
else:print("it is not a palindrome")

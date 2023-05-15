name = input("Enter your name")
firstLetter = "3"
name = name.replace(name[0], firstLetter)
print(name)



import datetime

def date_of_birth():
 date_of_birth = int(input("Enter a year "))
year_now = datetime.datetime.today()
current_year = year_now.year
age = current_year - date_of_birth
print(age)




add = 0
for num in range(10):
 add +=num
 print(add)



# with open("record.txt",mode='w') as file:
#     file.write("005 peter 78\n")
#     file.write("006 martins 76\n")
#     file.write("007 david 99\n")


# with open("product.txt", mode='r') as file:
#     for file in file:
#         num,name, score = file.split()
#         print(f"{num : < 10} {name : < 10} {score: >10}")


with open("student_record.txt", mode="a") as file:
    file.write("009 mimi 78 \n")

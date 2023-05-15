file1 = open("student_record.txt", mode="r")
file2 = open("record3.txt", mode="w")

with file1, file2:
    for record in file1:
        sn, name, score = record.split()
        if sn != "003":
            file2.write(record)
        else:
            new_record = ' '.join([sn, "iyowogoga", score])
            file2.write(new_record + "\n")

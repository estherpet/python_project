def multiply_number(multiply):
      for multiply_number in range (1,13):
        print(end=" ")
        for number in range (1,13):
          print(end=" "f"  {multiply_number: >3} x {number: >3} = {multiply_number * number: >3}")
        print()


multiply_number(13)


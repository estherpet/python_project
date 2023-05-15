def calculate_naira(dollar : int) ->str:
    amount = (input("Enter amount in $"))
    naira = 750 * amount()
    return f"The naira value is {naira}"

dollar = int(input("Enter dollar amount: "))
print(calculate_naira())
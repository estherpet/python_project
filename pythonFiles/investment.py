def investment(principal_amount,years):
    rate = 5
    count = 1

    while count <= years:
        roi = principal_amount * rate
        future_value = principal_amount + roi
        principal_amount = future_value
        print(f"year {count} return on investment is {roi},your principal is now {future_value}")
        count+=1


investment(20,4)

principal_amount = int(input("Enter the amount you want to invest :"))

years = int(input("Enter the number of years :"))

rate = 5

for year in range(1,years + 1):

    roi = principal_amount * rate

    future_value = principal_amount + roi

    principal_amount = future_value

    print(f"year {year} return on investment is {roi},your principal is now {future_value}")

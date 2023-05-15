def discount_price(amount):
    discount = 0.1 * amount
    new_price = discount - amount
    print(discount, new_price)
    amount = int(input("Enter amount :"))
    discount(amount)

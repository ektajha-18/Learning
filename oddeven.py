sale_amount=float(input("Enter the selling price: "))
cost_price=float(input("Enter the cost price: "))
if sale_amount>cost_price:
    profit_value=sale_amount-cost_price
    print("Its a profit, The profit amount is ", profit_value)
else:
    print("Its a loss")
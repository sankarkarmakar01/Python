# Write a program that will take user input of cost price and selling price and determines whether it's a loss or a profit

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if cost_price == selling_price:
    print("No Profit, No Loss")
elif cost_price < selling_price:
    print("Profit:", selling_price - cost_price)
else:
    print("Loss:", selling_price - cost_price)

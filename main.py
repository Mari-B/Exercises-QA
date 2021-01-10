product=input("enter the name of the product:")
price=input("enter the price:")
quantity=input("enter the quantity:")
amount=float(price)*float(quantity)
vat=amount*20/100
bill=amount+vat
print("--------------------")
print("your total amount is:",amount)
print("your vat is:",vat)
print("your bill is: £",bill)


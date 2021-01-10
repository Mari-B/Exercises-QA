a=1
while a<=100:
  if a%2==0:
    print(a, "even")
  else:
    print(a, "odd")
  a=a+1

t=1
while t<=10:
  print("times table of>",t)
  a=1
  while a<=10:
    print(t,"x",a,"=",(a*t))
    a=a+1
  t=t+1

a=1
sum=0
while a<=10:
  print(a)
  sum=sum+a
  a=a+1
print("sum of all numbers:", sum)

choice="y"
sum=0
while choice=="y" or choice=="Y":
  num=int(input("enter any number"))
  sum=sum+num
  choice=input("do you want to enter another value?")
print("the sum of all numbers:", sum)

choice="Y"
bill=0
while choice=="Y" or choice=="y":
  product=input("enter the product:")

  price=float(input("enter the price"))
  quantity=float(input("enter any number"))

  amount=price*quantity
  bill=bill+amount

  choice=input("is there another product?")

print("your bill is:",bill)

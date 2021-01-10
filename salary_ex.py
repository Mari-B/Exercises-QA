salary=float(input("enter your salary:"))
if salary >=2000:
  tax=salary*30/100
  net=salary-tax
if salary<2000:
  tax=salary*20/100
  net=salary-tax
print("your salary is:",salary)
print("your tax is:",tax)
print('your net salary is:',net)

salary=float(input("enter your salary:"))
if salary >=2000:
  tax=salary*30/100
  net=salary-tax
else:
  tax=salary*20/100
  net=salary-tax
print("your salary is:",salary)
print("your tax is:",tax)
print('your net salary is:',net)

salary=float(input("enter your salary:"))
if salary>2000:
  if salary>3000:
    tax=salary*30/100
  else:
    tax=salary*20/100
else:
  if salary>1000:
    tax=salary*10/100
  else:
    tax=0
net=salary-tax
print("Your Salary:",salary)
print("Your Tax:",tax)
print("Your Net Salary is:",net)
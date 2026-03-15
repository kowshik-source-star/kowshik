f=open("fin.txt","a")
from datetime import date
date=date.today()
income=int(input("Enter your Income - "))
expense=int(input("Enter the expense - "))
extra=input("Do you want to add extra expense? y or n - ")
while(extra=="y"):
    add=int(input("Enter the expense - "))
    expense=expense+add
    extra = input("Do you want to add extra expense? y or n - ")
        
balance=income-expense

f.write("\n"+"---"+str(date)+"---"+"\n")
f.write("Income = "+str(income)+"\n")
f.write("Expense = "+str(expense)+"\n")
f.write("Balance = "+str(balance))

f.close()

g=open("fin.txt","r")
print(g.read())
g.close()

# Program Name:  House_Income_Tax.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Due Date: 9/27/20
#Purpose: Determines user tax income based on income, martial status and elevation of house.

income = float(input("Enter income: ")) #input income amount
ms = int(input("Enter marital status (0.single/1.married):"))# Enter number to choose marital status
elevation = int(input("Enter elevation of the house (0.below sea level \ 1. at or above sea level):")) #Enter number to choose house elavation
tax = 0
#Calculate tax
if(income<10000):
    tax = (2.3*income)/100
elif(income>=10000 and income < 50000):
    tax = (4.5*income)/100
else:
    tax = (6.1*income)/100
if(ms==1):
    tax -= 24.62
if(elevation==0):
    tax += 18.32
print("Income tax: $" + str(tax)) #Print income tax
# Program Name:  Lab1.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 1 Due Date:     8/30/20
# Purpose: This program takes in the user input for the name of the grocery item and the price associated with it. Then a for loop runs through the arrays in order to print the name and price.

name = list() #set array
price = list() #set array
num = 8 #iteam number constant
print(" 8 items in checkout")
for i in range(int(num)): #go through the loop 8 times
    item_name = input("Enter name of item: ") #get names for each item
    name.append(item_name)  #attach name to array name
    item_price = input("Enter price for item: ") #get price for array
    price.append(item_price)  #attach price to array price
print("Product: ")
for i, j in zip(name, price): #for loop that uses 'zip' in order to comibne the cycle of the arrays
    print(i, j) #print price and name



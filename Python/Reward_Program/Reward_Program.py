# Program Name:  Reward_Program.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 2 Due Date:  9/13/20
# Purpose: This program takes in the user input for the name  and number of books purchased that month, then rewards
# customer with points based on amount entered.

CustomerName = input("Enter First and Last name: ")
BooksPurchased = int(input("Enter number of books purchased this month: "))
#customer purchases 0 books
if(BooksPurchased <= 0):
    print(CustomerName,"earned 0 points")
#customer purchases 1-3 books
elif(BooksPurchased <= 3):
    print(CustomerName, "earned 5 points")
#customer purchases 4-6 books
elif(BooksPurchased <= 6):
    print(CustomerName, "earned 10 points")
#customer purchases 7-8 books
elif(BooksPurchased <= 8):
    print(CustomerName, "earned 15 points")
#customer purchases 9 or more books
elif(BooksPurchased <= 9):
    print(CustomerName, "earned 20 points")
else:
    print(CustomerName, "earned 25 points")
# customer purchases 10 or more books

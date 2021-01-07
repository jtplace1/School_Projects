# Program Name:  Test_Grade_Average.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 2 Due Date:  10/18/20
# Purpose: This program takes in the user input for the name of 12 students and their 8 test grades,
# then displays the average and letter grade.
def calc_average(a1,a2,a3,a4,a5,a6,a7,a8): #Average function
    total=a1+a2+a3+a4+a5+a6+a7+a8 #calculating total
    avg = total/8 #calculating Average
    return (avg) 

def determine_grade(grade): # grade function
    if grade>=90 and grade<=100:
        let="A"
    elif grade>=80 and grade<=89.9:
        let="B"
    elif grade>=70 and grade<=79.9:
        let="C"
    elif grade>=60 and grade<=69.9:
        let="D"
    else:
        let="F"
    return (let) #return the grade

for x in range(1, 13): #loop for 12 students
    name=input("Enter the name: ")
    g1=int(input("Enter grade Test 1: "))
    g2=int(input("Enter grade Test 2: "))
    g3=int(input("Enter grade Test 3: "))
    g4=int(input("Enter grade Test 4: "))
    g5=int(input("Enter grade Test 5: "))
    g6=int(input("Enter grade Test 6: "))
    g7=int(input("Enter grade Test 7: "))
    g8=int(input("Enter grade Test 8: "))
    tp=calc_average(g1,g2,g3,g4,g5,g6,g7,g8)
    tp1=determine_grade(tp)
    print ("Student Name: ",name)
    print ("Average Score: ",tp)
    print ("Grade: ",tp1)
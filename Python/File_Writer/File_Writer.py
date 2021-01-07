# Program Name:  File_Writer.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 5 Due Date:  10/8/20
# Purpose: Gets user info saves it into text file then prints info within text file

#enter number of players.
num = int(input('Enter the number of players: '))
#Open the file to write
f = open('golf.txt', 'w')
for i in range(num):
    #enter the name.
    print ('Enter player name', i+1 ,':',end="");
    pname = input()
    #to enter the score.
    print ('Enter score of player', i+1 ,':',end="");
    pscore = int(input())
    if(pscore == 80):
        s = "Made par"
    elif (pscore < 80):
        s = "Under Par"
    elif (pscore > 80):
        s = "Over Par"
    #Write the name and score in the file.
    f.write(pname)
    f.write('\n')
    f.write(str(pscore))
    f.write('\n')
    f.write(s)
    f.write('\n')
#Close the file.
f.close();
# read the file
fopen = open('golf.txt', 'r')
print('---------------------------------------');
for i in fopen:
    #Display the data.
    print(i,end="")

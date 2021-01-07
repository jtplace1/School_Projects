# Program Name:  Rainfall.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 6 Due Date:     11/22/20
# Purpose: This program takes in the user input of rainfall for 12 months
# and finds the average, total, highest and lowest varibles from the info

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rfall = []
for i in range(12):
   val = float(input('Enter rainfall for ' + months[i] + ': '))
   rfall.append(val)


total = 0
avg = 0
low = 0
high = 0

for i in range(12):
   total += rfall[i]
   if rfall[i] < rfall[low]:
       low = i
   elif rfall[i] > rfall[high]:
       high = i

avg = total / 12
print()
print('Total rainfall: {:.1f} inches'.format(total))
print('Average rainfall: {:.1f} inches'.format(avg))
print('{} received the highest rainfall of {:.1f} inches'.format(months[high], rfall[high]))
print('{} received the lowest rainfall of {:.1f} inches'.format(months[low], rfall[low]))



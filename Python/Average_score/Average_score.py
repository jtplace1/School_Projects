# Program Name:  Average_score.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Due Date:     12/12/20
# Purpose: Finds the average score between 5 judges without the lowest and highest score.

def Average(Scores):

   high = max(Scores)
   low = min(Scores)

# remove highest and lowest scores

   av = (sum(Scores)-high-low)*1.0/(len(Scores)-2)

   return av

# stores the olympic score

Scores = []

i = 1

while i<=5:

    # Enter score of judges

    a = float(input("Please input the judge " + str(i) + " score: "))

    Scores.append(a)

    i = i + 1

# Print average score

print("The Average score without highest and lowest score: ",Average(Scores))
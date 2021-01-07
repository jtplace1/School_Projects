# Program Name:  Tuition.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Lab 3 Due Date:     10/04/20
#calculates the new tuition amount for each year
tuition = int(7180) #Initial tutition cost
rate = (3.5)/100 #the rate of increase per year
year = 2019 #Initial start year
for price in range(8): #increase the price throguh 8 itirations
    #Displays the year and the tuition cost per year formated to the nearest cent
    print("Tuition for", year, "school year ", '${:,.2f}'.format(tuition))
    #get the increased amount based on the tuition at that moment times the rate
    price = tuition * rate
    #gets new tutiion based on the price and the tuition from the previous year
    tuition = tuition + price
    #increase year by 1 to cycle through the 7 years
    year = year + 1
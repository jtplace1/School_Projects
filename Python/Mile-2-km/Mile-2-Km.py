# Program Name:  Test 2 p2.py
# Course:  IT1113/Section w01
# Student Name: Jabari Smith
# Assignment Number:  Test 2 Due Date:     10/25/20
def main():
    #enter the choice
    for x in range(0,15):
        choice = int(input("1. Miles to Kilometers \n2. Kilometers to Miles \nEnter 1 or 2: "))

        if choice == 1:
        # enter the distance in kilometers
            d_mile = float(input("\nEnter the distance: "))
            mile_to_km = Miles_to_Kilometers(d_mile)
        #distance in miles.
            print("\nMiles %.3f mile" % (d_mile))
        #converted distance in kilometers
            print("Kilometers %.3f km" % (mile_to_km))

        elif choice == 2:
            d_km = float(input("\nEnter the distance: "))
            km_miles = Kilometers_to_Miles(d_km)
        #distance in km.
            print("\nKilometers %.3f km" % (d_km))
        #converetd distance in kilometers.
            print("Miles %.3f mile" % (km_miles))

    #choice is not valid
        else:
            print("Invalid choice.")

# miles 2 kilometers.
def Miles_to_Kilometers(Distance):
    return Distance / 0.6214

# kilometers 2 miles.

def Kilometers_to_Miles(Distance):
    return Distance * 0.6214

main()
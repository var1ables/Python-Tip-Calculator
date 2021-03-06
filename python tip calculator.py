#Greeting
print("Welcome to the tip calculator!")

#Getting the total bill amount
bill = input("What was the total bill?")

#Getting the desired tip percentage
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15?")

#getting the number of people who ordered
guest = input("How many people to split the bill?")

#converting the tip percentage to a number which can be easily converted with the total
tip = float((float(tip_percent) / 100) + 1)

#Floating the str bill into a floating bill
bills = float(bill)

#Changing the str guest into a integer guests
guests = int(guest)

#Calculating the true bill amount from the floated string variables, rounding to the 2nd decimal
true_bill = round((bills * tip) / guests, 2)

#Displaying the true amount each person should pay
print(f"Each person should pay ${true_bill:.2f}")
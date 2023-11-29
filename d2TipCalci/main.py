#Tip Calculator
print("Welcome to the Tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
bill_with_tip = tip/100 * bill + bill
split = round(bill_with_tip/people,2)
print(f"Each person should pay: ${split}" )

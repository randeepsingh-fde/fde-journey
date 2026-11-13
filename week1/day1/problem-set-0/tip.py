bill = int(input("Enter the food cost: $"))
tip_percent = int(input("Enter the percentage of the bill you want to to leave as a tip: "))
tip = (tip_percent/100)*bill
print("The tip amount is: $", tip)
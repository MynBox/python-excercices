print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill ? "))
number_of_people = int(input("How many people were there ? "))
tip_percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
print(f"Each person should pay: {(total_bill * (tip_percentage/100) + total_bill)/number_of_people}")

input("Press [Enter] to exit")

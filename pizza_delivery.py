print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M, L ").lower()
add_pepperoni = input("Do you want pepperoni ? Y or N ").lower()
add_cheese = input("Do you want extra cheese ? Y or N ").lower()


bill = 0

if size == "s":
    bill += 15
    
elif size == "m":
    bill += 20
    
elif size == "l":
    bill += 25
else:
    print("Choose a correct size for your pizza.")
    


if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3




if add_cheese == "y":
    bill +=1




print(f"Your bill is {bill}")
input("To exit, press [Enter]")


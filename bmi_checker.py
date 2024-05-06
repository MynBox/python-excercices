height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight/height**2


if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}: You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}: You are in normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}: You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}: You are obese.")
else:
    print(f"Your BMI is {round(bmi)}: You are clinicaly obese.")


input("Press [Enter] to exit")

age = int(input("What's your age?"))
days_left = 90*365-age*365
weeks_left = 90*52-age*52
months_left = 90*12-age*12
years_left = 90-age
print(f"You have {days_left} days left, {weeks_left} weeks left, {months_left} months left and {years_left} years left")


birth_year = int(input("What year were you born in ? "))
age = 2023 - birth_year
print(f"Your are {age} years old.")

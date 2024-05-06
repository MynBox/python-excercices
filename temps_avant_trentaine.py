age = int(input("Quel est ton age ? "))
days_left = 30*365-age*365
weeks_left = 30*52-age*52
months_left = 30*12-age*12
years_left = 30-age
print(f"Il te reste {days_left} jours, {weeks_left} semaines, {months_left} mois and {years_left} années restants jusqu'à 30 ans \n")
input("Press[Enter]to exit")

import random
name_string = input("Give me everyone's names, separated by a comma. ")
names = name_string.split(", ")

number_people = len(names)-1
unfortunate_person = random.randint(0, number_people)

print(f"{names[unfortunate_person]} has to pay the bill")

input("Press [Enter] to exit")



import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose ? Press '0' for Rock, '1' for Paper, '2' for Scissors ")
if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("Wrong input")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if choice == "0":
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 2:
        print("You win!")
    else:
        print("You lose.")

if choice == "1":
    if computer_choice == 1:
        print("It's a draw")
    elif computer_choice == 0:
        print("You win!")
    else:
        print("You lose.")

if choice == "2":
    if computer_choice == 2:
        print("It's a draw")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("You lose.")

print("Press [Enter] to exit.")
    






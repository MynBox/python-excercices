import random

number = random.randint(1, 10)


end_game = False
while not end_game:
    guess = int(input("What number do you think, I chose ? "))
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too big.")
    else:
        print("You won!")
        cya = input("Do you want to play again ? If yes, type 'again' or 'quit' to exit ").lower()
        if cya == "again":
            number = random.randint(1, 10)
            print("Let's play again")
        else:
            print("bye")
            end_game = True

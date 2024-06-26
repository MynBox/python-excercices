#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


characters = ''
digits = ''
alpha = ''
for i in range(nr_letters):
    randomized_number = random.randint(0, len(letters)-1)
    characters += letters[randomized_number]

        
for i in range(nr_numbers):
    randomized_number = random.randint(0, len(numbers)-1)
    digits += numbers[randomized_number]
        
                
for i in range(nr_symbols):
    randomized_number = random.randint(0, len(symbols)-1)
    alpha += symbols[randomized_number]
                    
                        
passwd = characters+digits+alpha

print(passwd)





#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

mixed_passwd = list(passwd)
random.shuffle(mixed_passwd)
print("".join(mixed_passwd))


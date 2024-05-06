alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from cipher_art import logo
print(logo)


def caesar(text, shift, direction):
    if direction == "encode":
        
            code = ""

            
            for char in text:
                if char in alphabet: 
                    index = alphabet.index(char)
                    shifter_pro = index + (shift % 26)
                    code += alphabet[shifter_pro]

        

                else:
                    code += char
        
            print(f"The encoded message is {code}")

    elif direction == "decode":
        
            decode = ""

            
            for char in text:
                if char in alphabet: 
                    index = alphabet.index(char)
                    shifter_pro = index - (shift % 26)
                    decode += alphabet[shifter_pro]


                else:
                    decode += char
        
            print(f"The decrypted message is {decode}")

            
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
   
    
 

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.



            
end = False
while not end:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    
    continuer = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    
    if continuer == "yes":
        print("Let's go again!")
        
    elif continuer == "no":
        end = True
        print("Bye, love you.")
        exit()
        
    else:
        input("Wrong input! Press [Enter] to restart dialogue." ).lower()
        
        
    


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).



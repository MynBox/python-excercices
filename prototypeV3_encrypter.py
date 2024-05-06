alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesaer(text, shift, direction):
    if direction == "encode":
        
            code = ""

            
            for letter in text:
                if letter in alphabet: 
                    index = alphabet.index(letter)
                    shifter_pro = index + shift
                    if shifter_pro > 25:
                        shifter_pro = shifter_pro - 26
                
                    code += alphabet[shifter_pro]

        
                elif letter == " ":
                    code += " "
        
            print(f"The encoded message is {code}")

    elif direction == "decode":
        
            decode = ""

            
            for letter in text:
                if letter in alphabet: 
                    index = alphabet.index(letter)
                    shifter_pro = index - shift
                    decode += alphabet[shifter_pro]

            
                elif letter not in alphabet:
                    decode += " "
        
            print(f"The decrypted message is {decode}") 
        
      
        

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesaer(text, shift, direction)

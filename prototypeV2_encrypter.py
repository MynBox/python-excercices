alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text, shift):
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

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


def decrypt(text, shift):
    decode = ""
    for letter in text:
        if letter in alphabet: 
            index = alphabet.index(letter)
            shifter_pro = index - shift
            decode += alphabet[shifter_pro]
            
        elif letter not in alphabet:
            decode += " "
        
    print(f"The decrypted message is {decode}") 

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)

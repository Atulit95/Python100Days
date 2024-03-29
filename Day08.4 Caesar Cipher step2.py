alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(message,shift_value):
    encoded_message=""
    for i in range(len(message)):
        if message[i] in alphabet:
            position_in_alphabet=alphabet.index(message[i])
            encoded_message+=alphabet[shift_value+(position_in_alphabet)]
        else:
            encoded_message+= message[i]
    return print(f"Here is the encoded result: {encoded_message}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decode(message,shift_value):
    decoded_message=""
    for i in range(len(message)):
        if message[i] in alphabet:
            position_in_alphabet=alphabet.index(message[i])
            decoded_message+=alphabet[(26+position_in_alphabet)-shift_value]
        else:
            decoded_message+= message[i]
    return print(f"Here is the encoded result: {decoded_message}")



  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encode(message=text,shift_value=shift)
elif direction == "decode":
    decode(message=text,shift_value=shift)
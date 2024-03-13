alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encode() and decode() functions into a single function called caesar(). 

# def encode(message,shift_value):
#     encoded_message=""
#     for i in range(len(message)):
#         if message[i] in alphabet:
#             position_in_alphabet=alphabet.index(message[i])
#             encoded_message+=alphabet[shift_value+(position_in_alphabet)]
#         else:
#             encoded_message+= message[i]
#     return print(f"Here is the encoded result: {encoded_message}")

# def decode(message,shift_value):
#     decoded_message=""
#     for i in range(len(message)):
#         if message[i] in alphabet:
#             position_in_alphabet=alphabet.index(message[i])
#             decoded_message+=alphabet[(26+position_in_alphabet)-shift_value]
#         else:
#             decoded_message+= message[i]
#     return print(f"Here is the encoded result: {decoded_message}")

def caesar(message,shift_value,cipher_direction):
    converted_message=""
    for i in range(len(message)):
        if message[i] not in alphabet:
            converted_message+=message[i]
        if  message[i] in alphabet:
            position_in_alphabet = alphabet.index(message[i])
            if cipher_direction=="decode":
                converted_message+= alphabet[(26+position_in_alphabet)-shift_value]
            if cipher_direction=="encode":
               converted_message+= alphabet[shift_value+position_in_alphabet]    
    return print(f"Here is your {cipher_direction}d result: {converted_message}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(message=text,shift_value=shift,cipher_direction=direction)
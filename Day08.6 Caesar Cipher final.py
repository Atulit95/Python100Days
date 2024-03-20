import art_module
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

#TODO-1: Import and print the logo from art.py when the program starts.
print(art_module.cipher_art())

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

user_choice="yes"

while user_choice=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26
    caesar(message=text,shift_value=shift,cipher_direction=direction)
    user_choice =input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
print("Goodbye")

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
# In line 30 the term "%26" do the job required in TODO-2 

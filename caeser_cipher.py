# first craete a list of alphabets with their corresponding indices
alphabets = "abcdefghijklmnopqrstuvwxyz"

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)  # find the index of the character
            new_position = (position + shift_key) % 26  # shift index by the shift_key
            new_char = alphabets[new_position]  # find the character at the new position
            cipher_text += new_char
        else:
            cipher_text += char  # Leave non-alphabet characters unchanged
    print(f"The cipher text after encryption is: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)  
            new_position = (position - shift_key) % 26  
            new_char = alphabets[new_position]  
            plain_text += new_char
        else:
            plain_text += char  
    print(f"The plain text after decryption is: {plain_text}")

# create a loop to allow the user to perform multiple encryptions or decryptions
end_of_program = False
while not end_of_program:
    action_to_take = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))

    if action_to_take == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif action_to_take == "decrypt":
        decryption(cipher_text=text, shift_key=shift)

    keep_going = input("Type 'yes' to continue, type 'no' to exit:\n").lower()
    if keep_going == "no":
        end_of_program = True

print("Have a nice day: Bye...")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    shifted_text = ""
    for char in original_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift_amount) % 26
            shifted_text += alphabet[new_index]
    print(f"Here is the encoded result: {shifted_text}")

def decrypt(original_text, shift_amount):
    shifted_text = ""
    for char in original_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index - shift_amount) % 26
            shifted_text += alphabet[new_index]
    print(f"Here is the decoded result: {shifted_text}")

def caesar(direction , text , shift):
    if direction == 'encode':
        return encrypt(original_text=text, shift_amount=shift)
    elif direction == 'decode':
        return decrypt(original_text=text, shift_amount=shift)
    else:
        print("You should choose either \'encode\' or \'decode\'")
caesar(direction = direction, text = text , shift = shift)
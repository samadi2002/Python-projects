from art import logo

print(logo)

alphabet = [chr(i) for i in range(97, 123)]  # Generates a-z

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Keeps numbers/symbols unchanged

    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()

    if direction == "exit":
        print("Goodbye!")
        break

    if direction not in ["encode", "decode"]:
        print("Invalid option. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")

    if not shift.isdigit():  # Ensures shift is a valid number
        print("Invalid shift number. Please enter a positive integer.")
        continue

    shift = int(shift)

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1 & TODO-2: Create decrypt() and shift backwards
def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position - shift_amount) % 26
        decrypted_text += alphabet[new_position]

    print(decrypted_text)


# Existing encrypt function
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        cipher_text += alphabet[new_position]

    print(cipher_text)


# TODO-3: Combine encrypt and decrypt into caesar()
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        output_text += alphabet[new_position]

    print(output_text)


caesar(text, shift, direction)
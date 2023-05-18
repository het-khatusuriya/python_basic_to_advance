#Python program that implements a simple encryption and decryption algorithm called the Caesar cipher.
# The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet.

def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


# Example usage
plain_text = input("enter plain text: ")
shift = int(input("enter number for shifment process: "))

encrypted_text = encrypt(plain_text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)

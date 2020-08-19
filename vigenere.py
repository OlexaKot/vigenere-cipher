# Vigenere Cipher

# Setup
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Encryption
def encrypt(plaintext, keyword):
    ciphertext = ""
    key_indexes = []
    keyword = keyword.lower()
    for character in keyword:
        if character in alphabet:
            key_indexes.append((alphabet.index(character) + 1) % 26)
    current_key_index = 0
    for character in plaintext:
        is_upper = False
        if character.lower() in alphabet:
            if character not in alphabet:
                is_upper = True
                character = character.lower()
            encrypted_letter = alphabet[(alphabet.index(character) + key_indexes[current_key_index]) % 26]
            if is_upper == True:
                encrypted_letter = encrypted_letter.upper();
            ciphertext += encrypted_letter
            current_key_index += 1
            current_key_index = current_key_index % len(key_indexes)
        else:
            ciphertext += character
    print(ciphertext)

# Decryption
def decrypt(ciphertext, keyword):
    plaintext = ""
    key_indexes = []
    keyword = keyword.lower()
    for character in keyword:
        if character in alphabet:
            key_indexes.append((alphabet.index(character) + 1) % 26)
    current_key_index = 0
    for character in ciphertext:
        is_upper = False
        if character.lower() in alphabet:
            if character not in alphabet:
                is_upper = True
                character = character.lower()
            decrypted_letter = alphabet[(alphabet.index(character) - key_indexes[current_key_index]) % 26]
            if is_upper == True:
                decrypted_letter = decrypted_letter.upper();
            plaintext += decrypted_letter
            current_key_index += 1
            current_key_index = current_key_index % len(key_indexes)
        else:
            plaintext += character
    print(plaintext)

import math
import string
import sys

import numpy as np


def menu():
    while True:
        print("---- Hill Cipher ----\n")
        print("1) Encrypt a Message.")
        print("2) Decipher a Message.")
        print("3) Force a Ciphertext (Known Plaintext Attack).")
        print("4) Quit.\n")
        try:
            choice = int(input("Select a function to run: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("\nYou must enter a number from 1 to 4\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 4\n")


# Get input from the user and checks if they respect the alphabet
def get_text_input(message, alphabet):
    while True:
        text = input(message)
        text = text.upper()
        if all(keys in alphabet for keys in text):
            return text
        else:
            print("The text must contain only characters from the alphabet\n")


# Create the standard English alphabet and returns it
def get_alphabet():
    alphabet = {}
    for letter in string.ascii_uppercase:
        alphabet[letter] = string.ascii_uppercase.index(letter)
    return alphabet


# Create reverse dictionary for the alphabet and returns it
def get_reverse_alphabet(alphabet):
    reverse_alphabet = {}
    for key, value in alphabet.items():
        reverse_alphabet[value] = key
    return reverse_alphabet


# Check if the key is a square in length
def check_is_square(key, alphabet):
    while True:
        key_length = len(key)
        if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
            break
        else:
            print("The key must be a square and >= 2.\n")
            key = get_text_input("Insert the key for encryption: ", alphabet)


# Create the matrix K for the keys
def get_k_matrix(key, m, alphabet):
    array = []
    for character in key:
        array.append(alphabet[character])
    return np.matrix(np.reshape(array, (m, m)))


# Create the matrix of m-grams of the plaintext, if needed, complete the last m-gram with the first letter of the
# alphabet
def get_m_grams(plaintext, m, alphabet):
    array = []
    remainder = len(plaintext) % m
    for character in plaintext:
        array.append(alphabet[character])
    if remainder != 0:
        for i in range(m - remainder):
            array.append(0)
    mat = np.matrix(array)
    return mat.reshape((int(len(array) / m), m)).transpose()


# Encrypt a Message
def encrypt(plaintext, key, alphabet, reverse_alphabet):
    # Get m, length of the grams
    m = int(math.sqrt(len(key)))

    # Get the key matrix k
    k = get_k_matrix(key, m, alphabet)

    # Get the m-grams matrix p of the plaintext
    p = get_m_grams(plaintext, m, alphabet)
    m_grams = p.shape[1]

    # Encrypt the plaintext with the key provided k, calculate matrix c of ciphertext
    temp = []
    for i in range(m_grams):
        temp.append(np.dot(k, p[:, i]) % len(alphabet))
    c = np.column_stack(temp)

    # Transform the matrix c of ciphertext in letters from the alphabet
    ciphertext_array = np.ravel(c, order='F')
    ciphertext = ""
    for i in range(len(ciphertext_array)):
        ciphertext = ciphertext + reverse_alphabet[ciphertext_array[i]]

    return ciphertext


# Decrypt a Message
def decrypt(ciphertext, key, alphabet, reverse_alphabet):
    plaintext = ''

    return plaintext


# Force a Ciphertext (Known Plaintext Attack)
def plaintext_attack():
    return 0


def main():
    while True:
        # Ask the user what function wants to run
        choice = menu()

        # Get the standard English alphabet
        alphabet = get_alphabet()

        # Get the revers dictionary for the alphabet
        reverse_alphabet = get_reverse_alphabet(alphabet)

        # Run the function selected by the user
        if choice == 1:
            # Asks the user the text and the key for the encryption and checks the input
            plaintext = get_text_input("Insert the text to be encrypted: ", alphabet)
            key = get_text_input("Insert the key for encryption: ", alphabet)

            # Check if the key is quadratic
            check_is_square(key, alphabet)

            # Encrypt the plaintext
            ciphertext = encrypt(plaintext, key, alphabet, reverse_alphabet)

            print("\nThe message has been encrypted.")
            print("Generated Ciphertext: ", ciphertext, "\n")

        elif choice == 2:
            # Asks the user the text and the key for the encryption and checks the input
            ciphertext = get_text_input("Insert the text to be encrypted: ", alphabet)
            key = get_text_input("Insert the key for encryption: ", alphabet)

            # Check if the key is quadratic
            check_is_square(key, alphabet)

            # Check if the key is invertible
            # Continuare da qui!!!!..................................

            # Decrypt the ciphertext
            plaintext = decrypt(ciphertext, key, alphabet, reverse_alphabet)

            print("\nThe message has been decrypted.")
            print("Generated Plaintext: ", plaintext, "\n")

        elif choice == 3:
            plaintext_attack()
        elif choice == 4:
            sys.exit(0)


if __name__ == '__main__':
    main()

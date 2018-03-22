import math
import string
import sys

import numpy as np
from sympy import Matrix


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
def is_square(key, alphabet):
    while True:
        key_length = len(key)
        if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
            return key
        else:
            print("\nThe key must be a square and >= 2.\n")
            key = get_text_input("Insert the key for encryption: ", alphabet)


# Create the matrix K for the keys
def get_k_matrix(key, m, alphabet):
    array = []
    for character in key:
        array.append(alphabet[character])
    return np.matrix(np.reshape(array, (m, m)))


# Create the matrix of m-grams of a text, if needed, complete the last m-gram with the first letter of the alphabet
def get_m_grams(text, m, alphabet):
    array = []
    remainder = len(text) % m
    for character in text:
        array.append(alphabet[character])
    if remainder != 0:
        for i in range(m - remainder):
            array.append(25)
    mat = np.matrix(array)
    return mat.reshape((int(len(array) / m), m)).transpose()


# Encrypt a Message and returns the ciphertext and matrix c
def encrypt(k, p, alphabet, reverse_alphabet):
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

    return ciphertext, c


# Decrypt a Message and returns the plaintext and matrix p
def decrypt(k_inverse, c, alphabet, reverse_alphabet):
    m_grams = c.shape[1]

    # Decrypt the ciphertext with the key provided k, calculate matrix p of ciphertext
    temp = []
    for i in range(m_grams):
        temp.append(np.dot(k_inverse, c[:, i]) % len(alphabet))
    p = np.column_stack(temp)

    # Transform the matrix c of ciphertext in letters from the alphabet
    plaintext_array = np.ravel(p, order='F')
    plaintext = ''
    for i in range(len(plaintext_array)):
        plaintext = plaintext + reverse_alphabet[plaintext_array[i]]

    return plaintext, p


# Force a Ciphertext (Known Plaintext Attack)
def plaintext_attack(c, p_inverse, alphabet, reverse_alphabet):
    m_grams = c.shape[1]

    # Decrypt the ciphertext with the key provided k, calculate matrix p of ciphertext
    temp = []
    for i in range(m_grams):
        temp.append(np.dot(c, p_inverse[:, i]) % len(alphabet))
    k = np.column_stack(temp)

    # Transform the matrix c of ciphertext in letters from the alphabet
    key_array = np.ravel(k, order='F')
    key = ''
    for i in range(len(key_array)):
        key = key + reverse_alphabet[key_array[i]]

    return key, k


# Check if the key is invertible and in that case returns the inverse of the matrix
def is_invertible(matrix, alphabet):
    alphabet_len = len(alphabet)
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix_inverse = Matrix(matrix)
        matrix_inverse = np.matrix(matrix_inverse.inv_mod(alphabet_len))
        return matrix_inverse
    else:
        return None


def get_m():
    while True:
        try:
            m = int(input("Insert the length of the grams (m): "))
            if m >= 2:
                return m
            else:
                print("\nYou must enter a number m >= 2\n")
        except ValueError:
            print("\nYou must enter a number m >= 2\n")


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
            # Asks the user the plaintext and the key for the encryption and checks the input
            plaintext = get_text_input("Insert the text to be encrypted: ", alphabet)
            key = get_text_input("Insert the key for encryption: ", alphabet)

            # Check if the key is quadratic
            key = is_square(key, alphabet)

            # Get m, length of the grams
            m = int(math.sqrt(len(key)))

            # Get the key matrix k
            k = get_m_grams(key, m, alphabet)

            # Get the m-grams matrix p of the plaintext
            p = get_m_grams(plaintext, m, alphabet)

            # Encrypt the plaintext
            ciphertext = encrypt(k, p, alphabet, reverse_alphabet)

            print("\nThe message has been encrypted.")
            print("Generated Ciphertext: ", ciphertext[0], "\n")

        elif choice == 2:
            # Asks the user the ciphertext and the key for the encryption and checks the input
            ciphertext = get_text_input("Insert the ciphertext to be decrypted: ", alphabet)
            key = get_text_input("Insert the key for decryption: ", alphabet)

            # Check if the key is quadratic
            is_square(key, alphabet)

            # Get m, length of the grams
            m = int(math.sqrt(len(key)))

            # Get the key matrix k
            k = get_m_grams(key, m, alphabet)

            # Check if the key is invertible and in that case returns the inverse of the matrix
            k_inverse = is_invertible(k, alphabet)

            if k_inverse is not None:
                # Get the m-grams matrix c of the ciphertext
                c = get_m_grams(ciphertext, m, alphabet)

                # Decrypt the ciphertext
                plaintext = decrypt(k_inverse, c, alphabet, reverse_alphabet)
                print("\nThe message has been decrypted.")
                print("Generated Plaintext: ", plaintext[0], "\n")
            else:
                print("\nThe matrix of the key provided is not invertible.\n")

        elif choice == 3:
            # Asks the user the text and the ciphertext to use them for the plaintext attack
            plaintext = get_text_input("Insert the plaintext for the attack: ", alphabet)
            ciphertext = get_text_input("Insert the ciphertext of the plaintext for the attack: ", alphabet)

            # Asks the user the length of the grams
            m = get_m()

            # Get the m-grams matrix p of the plaintext and takes the firsts m
            p = get_m_grams(plaintext, m, alphabet)
            p = p[:, 0:m]

            # Check if the matrix of the plaintext is invertible and in that case returns the inverse of the matrix
            p_inverse = is_invertible(p, alphabet)

            if p_inverse is not None:
                # Get the m-grams matrix c of the ciphertext
                c = get_m_grams(ciphertext, m, alphabet)
                c = c[:, 0:m]

                # Decrypt the ciphertext
                key = plaintext_attack(c, p_inverse, alphabet, reverse_alphabet)
                print("\nThe key has been found.")
                print("Generated key: ", key[0], "\n")
            else:
                print("\nThe matrix of the plaintext provided is not invertible.\n")

        elif choice == 4:
            sys.exit(0)


if __name__ == '__main__':
    main()

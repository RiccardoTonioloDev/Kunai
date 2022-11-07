# Look at the shifting_by_key.py file
from shifting_by_key import shift_char_by_key, deshift_char_by_key


def vigenere_enc(data, key):
    # PRE: data is a string with only alphabetic chars; data is a string with only alphabetic chars
    # POST: encryption with vigenere algorithm
    cif_string = ""
    for i in range(len(data)):
        cif_string += shift_char_by_key(data[i], key[i % len(key)], 'a' if (
            ord(data[i]) >= ord('a') and ord(data[i]) <= ord('z')) else 'A')
    return cif_string


def vigenere_dec(data, key):
    # PRE: data is a string with only alphabetic chars; data is a string with only alphabetic chars
    # POST: decryption with vigenere algorithm
    cif_string = ""
    for i in range(len(data)):
        cif_string += deshift_char_by_key(data[i], key[i % len(key)], 'a' if (
            ord(data[i]) >= ord('a') and ord(data[i]) <= ord('z')) else 'A')
    return cif_string


# USAGE
print(vigenere_dec(vigenere_enc('provaprova', 'cesare'), 'cesare'))

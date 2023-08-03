
def decode_vignere_cipher(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_index = 0
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
        else:
            c_index = alphabet.index(ciphertext[i])
            k_index = alphabet.index(key[key_index % len(key)])
            shift = (c_index - k_index) % len(alphabet)
            plaintext += alphabet[shift]
            key_index += 1
    return(plaintext)

if __name__ == "__main__":
    ciphertext = "NCQXMIF GBVT HYDBQFBG DCQT"
    key = "ANYA"
    print(decode_vignere_cipher(ciphertext, key))

    key = "DOG"
    print(decode_vignere_cipher(ciphertext, key))

    key = "BOND"
    print(decode_vignere_cipher(ciphertext, key))


## Task: To find the private key d given the public key (n, e). The private key d is used to decrypt the Encrypted Message to get the flag.

"""
Hint: Encrypted Message needs to be converted to a number first. The number is then decrypted using the private key d and n. 
Anya can only count to 3 digits.
"""

def prime_factors(n):
    # TODO: Modify to return the prime factors of a number n
    factors = []
    return factors

def decrypt(ciphertext, d, n):
    # TODO: Modify to decrypt ciphertext using the private key d and n
    plaintext = ""
    return plaintext

def solve(encrypted_message, encrypted_n, encrypted_e):
    # TODO: Modify to return the flag
    mapping = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "X": 0
    }


    flag = ""
    return flag

if __name__ == "__main__":
    # Get encrypted_n and encrypted_e from Challenge 2
    encrypted_message = "AABI BAFI BE ACHC IFH CEBG CIBA CI AHAX HGE BHED IAD AHAX AFHA AFBF AXCE DGB CIBA AXCE CAFD ADA"
    encrypted_n = ""
    encrypted_e = ""

    rsa = solve(encrypted_message, encrypted_n, encrypted_e)
    print(rsa)
## Proposal side of generating m', c and c'. This is not given to users
import os

def XOR(a, b):
    r = b""
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, "big")
    return r


def gen_OTP(length):
    return bytearray(os.urandom(length))


def decrypt(cipher, OTP):
    """Decryption also using XOR, do not modify"""
    return XOR(cipher, OTP)

# Original plaintext and modified plaintext 
original_plaintext = b"https://pasteboard.co/pyPpJMZ58Ucv.jpg"
modified_plaintext = b"Find the URL"

# Randomly generated OTP
OTP = gen_OTP(length=len(original_plaintext))

# Generate c
original_cipher = XOR(original_plaintext, OTP)

# Generate mask
padded_modified_plaintext = b'\x00' * (len(original_plaintext) - len(modified_plaintext)) + modified_plaintext
mask = XOR(original_plaintext, padded_modified_plaintext)

# Generate c'
modified_cipher = XOR(original_cipher, mask)


## Check solutions
def check_hints():
    if (XOR(original_cipher, modified_cipher)!= mask):
        print("c' XOR c = mask: False")
        return ("Hints are wrong")
    elif (XOR(mask, padded_modified_plaintext)!= original_plaintext):
        print("Mask XOR m' = m: False")
        return ("Hints are wrong")
    else:
        return (f"""Hints are correct. 
                The given hints to users are m',c,c' which are as follows: 
                modified plaintext:{modified_plaintext},
                original cipher:{original_cipher},
                modified cipher:{modified_cipher}
                  """)
    
print(check_hints())

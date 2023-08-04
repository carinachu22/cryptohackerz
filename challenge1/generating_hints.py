## Proposal side of generating m', c and c'. This is not given to users
import os

def XOR(a, b):
    r = b""
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, "big")
    return r

# Original plaintext and modified plaintext 
original_plaintext = b"https://pasteboard.co/OLW6IDbNuqR1.png"
modified_plaintext = b"Find the URL"

# OTP
OTP = bytearray(b'!\xcb\x19}:\xa1v>c\x8b\xda\x8b\xe6\xe38e\xb50\x9d\x93\xf8\x1b\x7f-N\x9f1\xcb\xa7v:\xbc\x04\x00N\xdc\xa3Q')

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

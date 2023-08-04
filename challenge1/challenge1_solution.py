## Task: To find the original plaintext m given m'(modified_plaintext), c (original_cipher), c'(modified_cipher)
## Solution: Either solution 1 or solution 2 will give the correct original plaintext (m), which is a url used for challenge 2

# Given Information
modified_plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Find the URL'
original_cipher = b'I\xbfm\rI\x9bY\x11\x13\xea\xa9\xff\x83\x81W\x04\xc7T\xb3\xf0\x974\x0fT\x1e\xef{\x86\xfdC\x02\xe9gv`\xb6\xd36' 
modified_cipher = b'!\xcb\x19}:\xa1v>c\x8b\xda\x8b\xe6\xe38e\xb50\x9d\x93\xf8\x1b\x7f-N\x9fw\xa2\xc9\x12\x1a\xc8len\x89\xf1\x1d'

# XOR function
def XOR(a, b):
    r = b""
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, "big")
    return r

def solution1():
    mask = XOR(original_cipher, modified_cipher)
    original_plaintext_1 = XOR(mask, modified_plaintext)
    original_plaintext_1 = original_plaintext_1.decode()
    return original_plaintext_1

def solution2():
    k = XOR(modified_plaintext, modified_cipher)
    original_plaintext_2 = XOR(original_cipher, k)
    original_plaintext_2 = original_plaintext_2.decode()
    return original_plaintext_2

if __name__ == "__main__":
    # Solution 1
    print("Solution 1 returns ", solution1())    

    # Solution 2 
    print("Solution 2 returns ", solution1())    
    

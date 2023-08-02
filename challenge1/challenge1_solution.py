## Task: To find the original message m given m'(modified_plaintext),c (original_cipher), c'(modified_cipher)

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

# Solution 1 
mask = XOR(original_cipher, modified_cipher)
original_message = XOR(mask, modified_plaintext)
original_message = original_message.decode()
print(original_message)

# Solution 2 
k = XOR(modified_plaintext, modified_cipher)
message = XOR(original_cipher, k)
message = message.decode()
print(message)

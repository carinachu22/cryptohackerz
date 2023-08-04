
## Task: To find the original plaintext m given m'(modified_plaintext), c (original_cipher), c'(modified_cipher)

"""
Hint: Modified plaintext (m’) is modified from the original plaintext (m) through a process that involves an OTP (k), but you may or may 
not need to find the OTP (k) to find the original plaintext (m). XOR operations are useful. The original plaintext (m) is a url that can be 
used for challenge 2.
"""

# Given Information
modified_plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Find the URL'
original_cipher = b'I\xbfm\rI\x9bY\x11\x13\xea\xa9\xff\x83\x81W\x04\xc7T\xb3\xf0\x9740a\x19\xa9x\x8f\xc58O\xcdV1`\xac\xcd6' 
modified_cipher = b'!\xcb\x19}:\xa1v>c\x8b\xda\x8b\xe6\xe38e\xb50\x9d\x93\xf8\x1b\x7f-N\x9fw\xa2\xc9\x12\x1a\xc8len\x89\xf1\x1d'




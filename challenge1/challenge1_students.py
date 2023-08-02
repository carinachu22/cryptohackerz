
## Task: To find the original message m given m'(modified_plaintext),c (original_cipher), c'(modified_cipher)

"""
Hint: Modified plaintext (m’) comes from the original message (m) encrypted with an OTP (k), but you may or may not need to find the 
OTP (k) to find the original message (m). XOR operations are useful. The original message (m) is a url that can be used for challenge 2.
"""

# Given Information
modified_plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Find the URL'
original_cipher = b'I\xbfm\rI\x9bY\x11\x13\xea\xa9\xff\x83\x81W\x04\xc7T\xb3\xf0\x974\x0fT\x1e\xef{\x86\xfdC\x02\xe9gv`\xb6\xd36' 
modified_cipher = b'!\xcb\x19}:\xa1v>c\x8b\xda\x8b\xe6\xe38e\xb50\x9d\x93\xf8\x1b\x7f-N\x9fw\xa2\xc9\x12\x1a\xc8len\x89\xf1\x1d'




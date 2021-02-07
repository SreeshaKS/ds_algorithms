import base64

MESSAGE = '''EFQABwYGFhsSTFNJUkICAQ0AH1RfUkIGHAQNDhIUBwBCU1JBTBYABgAAHg0FTF9TVQADFQcTHwBU Ul9FVAEPCAEWFgwHHw1GR1NUEwYNGg0XDh4WHBFCU1JBTAYdHgoGGA0FTF9TVRcEEQoIHwBUUl9F VBsADRZUXkVCFQcOTFNJUkISGgZATA4='''

KEY = 'For your eyes only!'

# result = []
# for i, c in enumerate(base64.b64decode(MESSAGE)):
#     print(i,c)
#     # result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

# print(''.join(result))

import base64
from itertools import cycle

message =  bytes(MESSAGE)

key = bytes("your")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
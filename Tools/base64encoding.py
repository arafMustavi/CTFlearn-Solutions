# THEORY of base64 https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# using base64 package

import base64

message = "This is a test message"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

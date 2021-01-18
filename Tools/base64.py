# THEORY of base64
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

# from Scratch
string = "Python"
base64line = ""
for element in string:
    # print(bin(ord(element)).replace("0b","0"))
    chunk = bin(ord(element)).replace("0b","0")
    # print(chunk)
    base64line +=chunk
print(base64line)
# line = '1234567890'
n = 6
chunk_in_6 = [base64line[i:i+n] for i in range(0, len(base64line), n)]
print(chunk_in_6)

# using base64 package
import base64
message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

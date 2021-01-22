# THEORY of base64 https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# from Scratch
string = "Python"
base64line = ""
for element in string:
    chunk = bin(ord(element)).replace("0b", "0")
    base64line += chunk
print(base64line)

encodeNumber = {
    '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5' '6' '7' '8' '9'
                                                      '10' '11' '12' '13' '14' '15' '16' '17' '18' '19'
                                                      '20' '21' '22' '23' '24' '25' '26' '27' '28' '29'
                                                      '30' '31' '32' '33' '34' '35' '36' '37' '38' '39'
                                                      '40' '41' '42' '43' '44' '45' '46' '47' '48' '49'
                                                      '50' '51' '52' '53' '54' '55' '56' '57' '58' '59'
                                                      '60' '61' '62': '+', '63': '/'}

n = 6
chunked_in_6 = [base64line[i:i + n] for i in range(0, len(base64line), n)]
for i in chunked_in_6:
    print(int(i, 2))

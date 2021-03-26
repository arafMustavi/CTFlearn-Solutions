number_list = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

result = ""

for number in number_list:
    result += chr(ord('A')+number - 1)
print( result )
Problem Name : Character Encoding

Problem Link : https://ctflearn.com/challenge/115

Problem Description : In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

Solution Approach :

- The codes are in HEX.
- Need to break it into ASCII

Pythonic Solution : 
```
def decipher(stringofNumbers):
	listofnumbers = stringofNumbers.split(" ")
	flag = ""
	for num in listofnumbers:
		converted = chr(int(num,16))
		flag += converted		
	return flag

cipherText = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
print(decipher(cipherText))

```

Online Solution Tool : https://v2.cryptii.com/hexadecimal/caesar

**The Flag is : ABCTF{45C11_15_U53FUL}**

******************************************************************
Problem Name : Hextroadinary

Problem Link : https://ctflearn.com/challenge/158

Problem Description : Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? 
(Your answer should start with 0x.)

0xc4115 0x4cf8

Solution Approach :

- The Clue is in the name ROX: which reverses back to XOR!
- You have to XOR two element
- Convert the XOR Result to HEX for matching the Result

Pythonic Solution : 

```flag = hex(0xc4115^0x4cf8)```

**The Flag is : CTFlearn{0xc0ded}**

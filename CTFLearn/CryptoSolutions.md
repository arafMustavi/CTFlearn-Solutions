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

```
flag = hex(0xc4115^0x4cf8)
```

**The Flag is : CTFlearn{0xc0ded}**

******************************************************************
Problem Name : Base 2 2 the 6

Problem Link : https://ctflearn.com/challenge/192

Problem Description : here are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9

	
Solution Approach :

- The Clue is in the name: Base 2 2 the 6 means BASE 2 ^ 6 which is base 64
- You have to find the base64 text's ASCII value

Web Link to decipher:

https://www.base64decode.org/


**The Flag is : CTF{FlaggyWaggyRaggy}**

******************************************************************
Problem Name : Reverse Polarity

Problem Link : https://ctflearn.com/challenge/230

Problem Description :  I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101
	
Solution Approach :

- Convert the Binary String to ASCII Value

Web Link to decipher:

https://www.rapidtables.com/convert/number/binary-to-ascii.html

**The Flag is : CTF{Bit_Flippin}**

******************************************************************
Problem Name : Vigenere Cipher

Problem Link : https://ctflearn.com/challenge/305


Web Link to decipher:

https://www.dcode.fr/vigenere-cipher

**The Flag is : flag{CiphersAreAwesome}**


******************************************************************
Problem Name : Modern Gaius Julius Caesar

Problem Link : https://ctflearn.com/challenge/885

Problem Description : One of the easiest and earliest known ciphers but with XXI century twist! Nobody uses Alphabet nowadays right? Why should you when you have your keyboard?

BUH'tdy,|Bim5y~Bdt76yQ

Solution Approach :
- Look into your keyboard
- The Flag Starts with B and C is just 2 left shift.
- Shift all the Characters

**The Flag is : CTFlearn{Cyb3r_Cae54r}**

******************************************************************
Problem Name : Morse Code

Problem Link : 

Problem Description : 
..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...

Web Link to decipher: https://morsecode.world/international/translator.html

**The Flag is : {FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES}**

******************************************************************
Problem Name : 

Problem Link : 

Problem Description : 

Solution Approach :

Web Link to decipher:

**The Flag is : **

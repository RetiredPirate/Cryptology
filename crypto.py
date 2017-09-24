import io
import sys
from string import ascii_lowercase as alphabet
import string


def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    if type(plainText) is not str:
        return "Invalid Input, Must be a String"
    plainText = plainText.lower().replace(" ","")
    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(alphabet.index(letter)+aMap)%26-aMap])
    print(''.join(cipherText).upper())

def maDecrypt(cipherText):
    

import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
# import numpy


def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    if type(plainText) is not str:
        return "Invalid Input, Must be a String"
    plainText = plainText.lower().replace(" ","")

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(alphabet.index(letter)+aMap)%26-aMap])
    print(''.join(cipherText).upper())

def maDecrypt(cipherText, aMap = 1): # currently assumes aMap = 0
    if type(cipherText) is not str:
        return "Invalid Input, Must be a String"
    cipherText = cipherText.lower().replace(" ","")

    letterCount = []
    for letter in alphabet:
        letterCount.append(cipherText.count(letter))
    print letterCount

    maxLetterCount = max(letterCount)
    x = [i for i,j in enumerate(letterCount) if j == maxLetterCount]
    print(alphabet[x[0]])
    print(x)

def numMap(text, aMap = 1):
    text = stringCheck(text)
    numberList = []
    for letter in text:
        numberList.append(alphabet.index(letter)+aMap)
    return numberList

def stringCheck(text):
    if type(text) is not str:
        print "Invalid Input, Must be a String"
        return None

    text = re.sub(r'[^a-zA-Z]', '', text)
    text = text.lower().replace(" ","")
    return text

def spaceString(list):
    newString = ""
    for number in list:
        newString += " " + str(number)

    return newString

print(spaceString(numMap("XDY LYW ENG XDW NKS QWX YBW IYA KGG FMD YYE Y", aMap = 1)))
maDecrypt("XDY LYW ENG XDW NKS QWX YBW IYA KGG FMD YYE Y")
print((-18)%26)
print(maEncrypt("XDY LYW ENG XDW NKS QWX YBW IYA KGG FMD YYE Y", lambda x: (19*x + 0)%26  , aMap = 0))

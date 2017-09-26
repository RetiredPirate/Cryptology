import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
import numpy


def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    if type(plainText) is not str:
        return "Invalid Input, Must be a String"
    plainText = plainText.lower().replace(" ","")

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(alphabet.index(letter)+aMap)%26-aMap])
    print(''.join(cipherText).upper())

def maDecrypt(cipherText):
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



print(numMap("I love deadlines. I love the whooshing noise they make as they go by.", aMap = 0))

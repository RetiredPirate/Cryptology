import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
import numpy
import pylatex


def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    plainText = stringCheck(plainText)
    plainText = numMap(plainText, aMap)

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(letter)%26-aMap])
    print(''.join(cipherText).upper())

def maDecrypt(cipherText, aMap = 1):
    cipherText = stringCheck(cipherText)

    letterCount = []
    for letter in alphabet:
        letterCount.append(cipherText.count(letter))
    print(letterCount)

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
        print("Invalid Input, Must be a String")
        return None

    text = re.sub(r'[^a-zA-Z]', '', text)
    text = text.lower().replace(" ","")
    return text


def hillDecrypt(cipherText, aMap = 1):
    text = stringCheck(text)
    text = numMap(text, aMap)






print(maEncrypt("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
        yhf rno ipy bzf rmk non kxu ffk maf fup hof vyg nan hop rlo noi npy bny \
        vpo xfu zfr mkn onu ffk h", lambda x: (9*x+9)%26 ))
print((18*21)%26)

# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 0))
# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 1))

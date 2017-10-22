import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
<<<<<<< HEAD
import numpy
import pylatex
=======
# import numpy
>>>>>>> 5f93bc6ff62325b001aca7b6d5c293f411ae4c10


def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    plainText = stringCheck(plainText)
    plainText = numMap(plainText, aMap)

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(letter)%26-aMap])
    print(''.join(cipherText).upper())

<<<<<<< HEAD
def maDecrypt(cipherText, aMap = 1):
    cipherText = stringCheck(cipherText)
=======
def maDecrypt(cipherText, aMap = 1): # currently assumes aMap = 0
    if type(cipherText) is not str:
        return "Invalid Input, Must be a String"
    cipherText = cipherText.lower().replace(" ","")
>>>>>>> 5f93bc6ff62325b001aca7b6d5c293f411ae4c10

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

def spaceString(list):
    newString = ""
    for number in list:
        newString += " " + str(number)

def hillDecrypt(cipherText, aMap = 1):
    text = stringCheck(text)
    text = numMap(text, aMap)






print(maEncrypt("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
        yhf rno ipy bzf rmk non kxu ffk maf fup hof vyg nan hop rlo noi npy bny \
        vpo xfu zfr mkn onu ffk h", lambda x: (9*x+9)%26 ))
print((18*21)%26)


<<<<<<< HEAD
print(spaceString(numMap("ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT \
        XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY \
         EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P", aMap = 0)))

maDecrypt("ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT \
        XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY \
         EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P")


maEncrypt("ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT \
        XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY \
         EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P", lambda x: (25*x-23)%26)

# print((-18)%26)
# print(maEncrypt("HGH FJL IOF YJJ TXN YJI HON VHC DJL IOW XFY XXT XON V", lambda x: (3*(x - 13))%26 , aMap = 0))
=======
# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 0))
# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 1))
>>>>>>> 2481adecd52191ddf465b30a11ea27025ec1c842

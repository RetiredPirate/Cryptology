import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
# import pylatex
# import numpy



def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    plainText = stringCheck(plainText)
    plainText = numMap(plainText, aMap)

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(letter)%26-aMap])
    return (''.join(cipherText).upper())

def freqInfo(cipherText, aMap = 1):
    cipherText = stringCheck(cipherText)

    letterCount = []
    for letter in alphabet:
        letterCount.append(cipherText.count(letter))

    maxLetterCount = max(letterCount)
    x = [i for i,j in enumerate(letterCount) if j == maxLetterCount]
    print(alphabet[x[0]])
    print(x)

def digraphFreq(cipherText, aMap = 1):
    cipherText = numMap(stringCheck(cipherText))




# def kasiskiTest(cipherText, aMap=1):
#     cipherText = numMap(stringCheck(cipherText))
#
#     listOfSubstrings = []
#     for substringLen in range(3,len(cipherText)):
#         for num in range(0, len(cipherText)-substringLen):
#             newString = cipherText[num:num+substringLen]
#             if newString not in listOfSubstrings:
#                 listOfSubstrings.append((newString, 0))
#             else:
#                 listOfSubstrings[index(newString)]

    return listOfSubstrings

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

    return newString

def hillDecrypt(cipherText, aMap = 1):
    text = stringCheck(text)
    text = numMap(text, aMap)


def vignereEncrypt(plainText, keyWord, aMap = 1):
    plainText = numMap(stringCheck(plainText), aMap)
    keyWord = numMap(stringCheck(keyWord), aMap)

    keyLen = len(keyWord)
    cipherText = ""

    for i in range(0,len(plainText)):
        cipherText += alphabet[plainText[i] + keyWord[i%keyLen]]

    return cipherText

def vignereDecrypt(plainText, keyWord, aMap = 1):
    plainText = numMap(stringCheck(plainText), aMap)
    keyWord = numMap(stringCheck(keyWord), aMap)

    keyLen = len(keyWord)
    cipherText = ""

    for i in range(0,len(plainText)):
        cipherText += alphabet[plainText[i] - keyWord[i%keyLen]]

    return cipherText




#
# print(vignereEncrypt("cheesyfeet", "apple", aMap = 0))
#
# print(vignereDecrypt("TUL VCA CTY CFW PGC BW", "berry", aMap = 0))

# print(kasiskiTest("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
#         yhf rno ipy bzf rmk non kxu ffk maf fup hof vyg nan hop rlo noi npy bny \
#         vpo xfu zfr mkn onu ffk h"))
# print((19*4)%26)

# print(spaceString(numMap("KFH YYG IGM CEJ SST EBO EUG RWJ TSD VYK ZOZ LIZ KFH XKU UIC WXF WJG AXQ PBQ AGV GXD VDG UEV GMI GYK QQP IPS CLL FYP MUL KFH XPM HGM EVD KAV YQC EGU EAL YYY ZSZ MPX ZOC TXT RIM DID VDG SXO ZFF TSM EDV MEI MDV MPK OUJ KOD UBO AXB OOR SLP ZCW IMD VYG JWM IFQ", aMap = 1)))
# freqInfo("KFH YYG IGM CEJ SST EBO EUG RWJ TSD VYK ZOZ LIZ KFH XKU UIC WXF WJG AXQ PBQ AGV GXD VDG UEV GMI GYK QQP IPS CLL FYP MUL KFH XPM HGM EVD KAV YQC EGU EAL YYY ZSZ MPX ZOC TXT RIM DID VDG SXO ZFF TSM EDV MEI MDV MPK OUJ KOD UBO AXB OOR SLP ZCW IMD VYG JWM IFQ")

print(maEncrypt("a common mistake", lambda x: ((x * 7) + 5)%26).lower())

# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 0))
# print(numMap("abcdefghijklmnopqrstuvwxyz", aMap = 1))

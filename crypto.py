import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
# import pylatex
# import numpy



################################################################################
#
# maEncrypt(plainText, cipher, aMap)
#
# returns the text enciphered by the given monoalphabetic cipher.
#   May also be used to decrypt text with a known key.
#
# cipherText: a string of enciphered text
# aMap: the number in the ring Z26 that should map to the letter A
#
################################################################################
def maEncrypt(plainText, cipher = lambda x: (x**5)%26, aMap = 1):
    """Return the text enciphered by the given cipher."""

    plainText = stringCheck(plainText)
    plainText = numMap(plainText, aMap)

    cipherText = []
    for letter in plainText:
        cipherText.append(alphabet[cipher(letter)%26-aMap])
    return (''.join(cipherText).upper())



################################################################################
#
# freqInfo(cipherText)
#
# returns a list of each letter in the alphabet with the number of
#   appearances in the given cipherText string.
#
# cipherText: a string of enciphered text
#
################################################################################
def freqInfo(cipherText):
    """Return a list of each letter with its count."""

    cipherText = stringCheck(cipherText)

    letterCount = []
    for letter in alphabet:
        letterCount.append(cipherText.count(letter))

    # TODO: make this a dict instead of a list
    printList = []
    for letter in range(len(alphabet)):
        printList.append((alphabet[letter],letterCount[letter]))

    return list(reversed(sorted(printList, key = lambda x: x[1])))


# Incomplete implementation. TODO
def digraphFreq(cipherText, aMap = 1):
    cipherText = numMap(stringCheck(cipherText))



# Incomplete implementation. TODO
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


################################################################################
#
# vignereFreq(cipherText, kenLen)
#
# splits the cipherText into columns corresponding to the keyLen and
#   returns a freqency analysis for each column.
#
# cipherText: a string of enciphered text
# keyLen: the integer length of the key word
#
################################################################################
def vignereFreq(cipherText, keyLen):
    """Return freqency analysis for each column."""

    cipherText = stringCheck(cipherText)

    column = 0
    columnMatrix = ["" for i in range(keyLen)]
    for letter in cipherText:
        columnMatrix[column] += (letter)

        column += 1
        if column >= 5:
            column = 0

    retList = []
    for string in columnMatrix:
        retList.append(freqInfo(string))

    return retList
    #TODO: split cipherText into columns as well and compare to freqInfo

    # print(columnMatrix)







# print(maEncrypt("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
#         yhf rno ipy bzf rmk non kxu ffk maf fup hof vyg nan hop rlo noi npy bny \
#         vpo xfu zfr mkn onu ffk h", lambda x: (x-11)%26 ))
# print((18*21)%26)
#

# maDecrypt("MFE RLH WSR LHW BZN BNW SRX DEC INQ RNW JHL RBW BNL DER HQN DEQ \
#             BUJ WSH UZS RNN LDE RDA HJH LQC RWS HUM DTR EHU ICH NWN CDU JRE \
#             WSH ULD UDM DCP BWN AER RBW ZHU QRM CHP RIH UPX SRE RHE ZSB LRI \
#             RNI BIB WBU HQH WSW FQ")
#
#
# maEncrypt("MFE RLH WSR LHW BZN BNW SRX DEC INQ RNW JHL RBW BNL DER HQN DEQ \
#             BUJ WSH UZS RNN LDE RDA HJH LQC RWS HUM DTR EHU ICH NWN CDU JRE \
#             WSH ULD UDM DCP BWN AER RBW ZHU QRM CHP RIH UPX SRE RHE ZSB LRI \
#             RNI BIB WBU HQH WSW FQ", lambda x: ((3*x)-7)%26 , aMap=1)

vignereFreq("jsfalsjdlfkjalfhdksajhlfdkjha", 5)

print("jsfalsjdlfkjalfhdksajhlfdkjha")

# print((-18)%26)
# print(maEncrypt("HGH FJL IOF YJJ TXN YJI HON VHC DJL IOW XFY XXT XON V", lambda x: (3*(x - 13))%26 , aMap = 0))

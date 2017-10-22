import io
import sys
from string import ascii_lowercase as alphabet
import string
import re
# import numpy


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
    # print(letterCount)

    # maxLetterCount = max(letterCount)
    # x = [i for i,j in enumerate(letterCount) if j == maxLetterCount]
    printList = []
    for letter in range(len(alphabet)):
        printList.append((alphabet[letter],letterCount[letter]))

    # sorted(printList, key = lambda x: x[1])
    print(reversed(sorted(printList, key = lambda x: x[1])))
    # print(alphabet[x[0]])

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






# print(maEncrypt("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
#         yhf rno ipy bzf rmk non kxu ffk maf fup hof vyg nan hop rlo noi npy bny \
#         vpo xfu zfr mkn onu ffk h", lambda x: (x-11)%26 ))
# print((18*21)%26)
#

print(spaceString(numMap("ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT \
        XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY \
         EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P", aMap = 0)))

maDecrypt("MFE RLH WSR LHW BZN BNW SRX DEC INQ RNW JHL RBW BNL DER HQN DEQ \
                BUJ WSH UZS RNN LDE RDA HJH LQC RWS HUM DTR EHU ICH NWN CDU JRE \
                WSH ULD UDM DCP BWN AER RBW ZHU QRM CHP RIH UPX SRE RHE ZSB LRI \
                RNI BIB WBU HQH WSW FQ")


maEncrypt("ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT \
        XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY \
         EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P", lambda x: (x-11)%26 )

# print((-18)%26)
# print(maEncrypt("HGH FJL IOF YJJ TXN YJI HON VHC DJL IOW XFY XXT XON V", lambda x: (3*(x - 13))%26 , aMap = 0))

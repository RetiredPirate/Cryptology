import io
import sys
from string import ascii_lowercase
import string
import re
# import pylatex
# import numpy


################################################################################
#                           Static Functions
################################################################################


def texTable(text):
    """Insert '&' between each list entry to format for LaTeX lables"""
    out = text[0]
    for letter in text[1:]:
        out += " & " + letter

    out += " \\\\"
    return out



def stringCheck(text):
    """Convert mixed case text to all lower case and remove spaces"""
    if type(text) is not str:
        print("Invalid Input, Must be a String")
        return None

    text = re.sub(r'[^a-zA-Z]', '', text)
    text = text.lower().replace(" ","")
    return text



def spaceString(list):
    """Add spaces between list numbers"""
    newString = ""
    for number in list:
        newString += " " + str(number)

    return newString



################################################################################
# class cipher:
#
#   difines a maping of the English alphabet
################################################################################
class cipher:

    def __init__(self, aMap = 1):
        """Initialize a new cipher object."""
        self.alphabet = []

        for i in range(26):
            self.alphabet.append(ascii_lowercase[(i-aMap)%26])

    def __str__(self):
        return self.alphabet


    ############################################################################
    # maEncrypt(plainText, cipher)
    #
    #   returns the text enciphered by the given monoalphabetic cipher.
    #       May also be used to decrypt text with a known key.
    #
    #   plainText: a string of unenciphered text
    #   cipher: function to map plainText to cipherText
    ############################################################################
    def maEncrypt(self, plainText, cipher = lambda x: (x**5)%26):
        """Return the text enciphered by the given cipher."""

        plainText = stringCheck(self.numMap(plainText))

        cipherText = []
        for letter in plainText:
            cipherText.append(self.alphabet[cipher(letter)%26])
        return (''.join(cipherText).upper())



    ############################################################################
    # freqInfo(cipherText)
    #
    #   returns a list of each letter in the alphabet with the number of
    #       appearances in the given cipherText string.
    #
    #   cipherText: a string of enciphered text
    ############################################################################
    def freqInfo(self, cipherText):
        """Return a list of each letter with its count."""

        cipherText = stringCheck(cipherText)

        letterCount = []
        for letter in self.alphabet:
            letterCount.append(cipherText.count(letter))

        # TODO: make this a dict instead of a list
        printList = []
        for letter in range(len(self.alphabet)):
            printList.append((self.alphabet[letter],letterCount[letter]))

        return list(reversed(sorted(printList, key = lambda x: x[1])))


    # Incomplete implementation. TODO
    # def digraphFreq(self, cipherText):
    #     cipherText = numMap(stringCheck(cipherText))
    #
    #
    #
    # Incomplete implementation. TODO
    # def kasiskiTest(self, cipherText):
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
    #
    #     return listOfSubstrings



    ############################################################################
    # numMap(text):
    #
    #   Maps the given text to numbers within the class specified alphabet
    #
    #   text: plain text using all lower case and no spaces
    #
    #   return: list of numbers corresponding to position withing the
    #               class alphabet
    ############################################################################
    def numMap(self, text):
        """Return list of numbers corresponding to given letters in alphabet"""
        text = stringCheck(text)
        numberList = []
        for letter in text:
            numberList.append(self.alphabet.index(letter))
        return numberList



    # Not implemented
    def hillDecrypt(self, cipherText):
        text = stringCheck(self.numMap(text))



    ############################################################################
    # vignereEncrypt(cipherText, keyWord):
    #
    #   Encrypts the plainText with the given key word by mathematical addition
    #
    #   plainText: a string of plain text
    #   keyWord: the string of characters representing the key
    ############################################################################
    def vignereEncrypt(self, plainText, keyWord):
        """Encrypt plain text with vignere cipher using given key word"""
        plainText = self.numMap(stringCheck(plainText))
        keyWord = self.numMap(stringCheck(keyWord))

        keyLen = len(keyWord)
        cipherText = ""

        for i in range(0,len(plainText)):
            cipherText += self.alphabet[(plainText[i] + keyWord[i%keyLen])%26]

        return cipherText



    ############################################################################
    # vignereDecrypt(cipherText, keyWord):
    #
    #   Decrypts the plainText with the given key word by mathematical subtraction
    #
    #   cipherText: a string of enciphered text
    #   keyWord: the string of characters representing the key
    ############################################################################
    def vignereDecrypt(self, cipherText, keyWord):
        """Decrypt cipher text with vignere cipher using given key word"""

        cipherText = self.numMap(stringCheck(cipherText))
        keyWord = self.numMap(stringCheck(keyWord))

        keyLen = len(keyWord)
        plainText = ""

        for i in range(0,len(cipherText)):
            plainText += self.alphabet[(cipherText[i] - keyWord[i%keyLen])%26]

        return plainText



    ############################################################################
    # vignereFreq(cipherText, kenLen)
    #
    #   splits the cipherText into columns corresponding to the keyLen and
    #       returns a freqency analysis for each column.
    #
    #   cipherText: a string of enciphered text
    #   keyLen: the integer length of the key word
    ############################################################################
    def vignereFreq(self, cipherText, keyLen):
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






################################################################################
#                           END OF CLASS: TESTS
################################################################################




newCipher = cipher(1)
# print newCipher.alphabet


print(texTable(newCipher.vignereEncrypt("hello world", "cheese")))

# print(newCipher.maEncrypt("lzf rrf yrp hol dno ilo mnf mkn rld njd nji nyo axp ybo fgc hpb \
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
#             RNI BIB WBU HQH WSW FQ", lambda x: ((3*x)-7)%26)

# vignereFreq("jsfalsjdlfkjalfhdksajhlfdkjha", 5)
#
# print("jsfalsjdlfkjalfhdksajhlfdkjha")

# print((-18)%26)
# print(maEncrypt("HGH FJL IOF YJJ TXN YJI HON VHC DJL IOW XFY XXT XON V", lambda x: (3*(x - 13))%26))

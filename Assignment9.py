from email.mime import image

import numpy as np
"""
Define an abstract class, BarcodeABC, that contains these abstract method signatures.  Any class that implements BarcodeABC is expected to store some version of an image and some version of the text associated with that image.

    scan(self, bc):
    readText(self, text):
    generateImageFromText(self):
    translateImageToText(self):
    displayTextToConsole(self):
    displayImageToConsole(self):

Now, as I said, this is an abstract class.  So you should be able to do this part of the assignment in less than 60 seconds.  I'll time you.  Go.
"""

from abc import ABC
import copy

class BarcodeABC(ABC):
    def scan(self, bc):
        pass
    def translateImageToText(self):
        pass
    def displayTextToConsole(self):
        pass
    def displayImageToConsole(self):
        pass
    def generateImageFromText(self):
        pass
    def translateImageToConsole(self):
        pass

class BarcodeImage(BarcodeABC):
    MAX_HEIGHT = 30
    MAX_WIDTH = 65
    imageData = [[0] * MAX_HEIGHT] * MAX_WIDTH
    def __init__(self, strData=None):
        self.strData = strData
        InfoBox.generateImageFromText(strData)
        for row in range(0,len(InfoBox.info)):
            for column in range(len(InfoBox.info[row]), 0, -1):
                self.imageData[row][column] = InfoBox.info[row][column]

    def getPixel(self, row, col):
        if row < 0 or row >= len(self.info) and col < 0 or col >= len(self.info[row]):
            return self.imageData[row][col]

    def setPixel(self, row, col, value):
        self.info[row][col] = value

class InfoBox(BarcodeABC):
    WHITE_CHAR = " "
    BLACK_CHAR = "*"
    DEFAULT_BARCODE = BarcodeImage()

    def __init__(self, image, text):
        if type(image) == BarcodeImage:
            self.scan(image)
        else:
            self.image = self.DEFAULT_BARCODE


    info = np.array([])
    def scan(self, bc):
        super().scan(bc)
        scannedbc = copy.deepcopy(bc)
        return  scannedbc


    def translateImageToText(self):
        super().translateImageToText()
        bob = self.scan
        text =""

        for i in range(0, len(self.image)):
            x = "0b"
            for j in range(0, len(self.image[i])):
                if info[i][j] == "*":
                    bob[i][j] = 1
                    x+= "1"
                elif info[i][j] == "":
                    bob[i][j] = 0
                    x += "0"
            add =  int(x, 2)
            text += add







      """"  
      for i in range(0, len(self.image)):
            for j in range(0, len(self.image[i])):
                if image[i][j] == 1:
                    bob[i][j] = "*"
                elif image[i][j] == 0:
                    bob[i][j] = ""
        
"""




    def readText(self, text):
        super().readText(text)
        if type(text) == str:
            self.text = text


    def generateImageFromText(self):
        super().generateImageFromText()
        image = np.array([])
        for i in range(0, len(self.text)):
            x = self.create_column(i, self.text[i])
            image = np.append(image, x)
        #if image exists, return true, else false in the variable bob
        return True

    def create_column(self, col, code):
        column = np.array([])
        ascii_value = ord(code)  # Gets the ASCII value (84 for 'T')
        binary_without_prefix = bin(ascii_value)[2:]
        j = len(binary_without_prefix)
        for i in range(0, j):
            column = np.append(column, binary_without_prefix[i])
        j -= 1
        column.reshape(1, j)
        return column





    def displayImageToConsole(self):
        print(self.scan)






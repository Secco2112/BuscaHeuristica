import minecart
import os

class GenerateMap:
    def __init__(self):
        self.file = ""

    def setFile(self, file):
        self.file = file
        return self

    def getFile(self):
        return self.file

    def parseFile(self):
        file = open(self.file, "rb")
        self.doc = minecart.Document(file)
        print(dir(self.doc.parser.data.title))


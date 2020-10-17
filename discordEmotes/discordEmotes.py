
#==================================================================
'''============================================================='''
'''============= With python and Pillow installed =============='''
'''=================== Copy and double click ==================='''
'''============================================================='''
#==================================================================

import PIL.Image as img
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

test = True
normalization = True 
maxsize = 128 #You can change this size tofit your own need

class imageFile:
    def __init__(self, inName = None, inExt = None):
        self.__extension = inExt;
        self.__name = inName;

    def setName(self, inName):
        self.__name = inName;

    def setExtension(self, inExt):
        self.__extension = inExt;

    def getName(self):
        return self.__name;

    def getExt(self):
        return self.__extension;

    def toString(self):
        return self.__name + self.__extension;

def reSize(inlist):
    smallEdge = int( min(inlist[0], inlist[1]) * maxsize / max(inlist[0], inlist[1]))
    if inlist[0] > inlist[1]:
        return maxsize, smallEdge
    elif inlist[0] < inlist[1]:
        return smallEdge, maxsize
    elif inlist[0] == inlist[1]:
        return maxsize, maxsize

def getCurrentFolder():
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            break;
    return dir

def findType(tarTypes = ["jpg","png"]):

    fileList = os.listdir(getCurrentFolder())

    imgFiles = []

    for f in fileList:
        for ext in tarTypes:
            if f.lower()[-len(ext):] == ext:
                newImg = imageFile(f[:len(f) - len(ext)], ext)
                imgFiles.append(newImg)
                print(newImg.toString())
                continue;

    return imgFiles

def emoConvert(imgFiles = [], targetFormat ="same"):

    outDir = getCurrentFolder() + '\\OutputImages\\'
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    # iterating through images 
    for currentImage in imgFiles:
        currentName = currentImage.getName();
        currentExt = currentImage.getExt();
        currentMode = "RGB"

        if currentExt in ["png"]:
            currentMode = "RGBA"

        im = img.open(currentName + currentExt).convert(currentMode) 

        #resizing 
        xSize, ySize = reSize(im.size)
        if test: print(xSize, ySize) 
        out = im.resize((xSize, ySize), img.ANTIALIAS)

        #overlay a square image if needed
        if normalization:
            squareImg = img.new(currentMode, (maxsize, maxsize), 
                                (0, 0, 0) if currentMode =='RGB' else (0, 0, 0, 0))
            squareImg.paste(out, (int((maxsize - xSize) / 2), int((maxsize - ySize) / 2)))
            out = squareImg

        # change extension if neeeded 
        extension = currentExt if targetFormat == "same" else targetFormat

        #saving 
        out.save(outDir + currentName + extension)

#==================================================================
'''============================================================='''

def Main():  

    try:
        waitingToConv = findType()
        emoConvert(waitingToConv)
    except (ValueError,NameError,SyntaxError,AttributeError,\
        TypeError) as err:
        print('Error!',err);


if __name__ == '__main__':
    Main()

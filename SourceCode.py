'''
                             Author:  AmarthGul
This script is orignally coded to resize images for telegram stickers making 
                    So it save images as .png and 512 pixels
  To start convert, you can place this file in the directorty of the images, 
     Then run this script, you'll get a new folder called 'OutputImages',
                    in which has a pile of images resized.
                        (You may need install pillow)
'''

import PIL.Image as img
import os

def reSize(inlist):
    smallEdge = int( min(inlist[0], inlist[1]) * 512 / max(inlist[0], inlist[1]))
    if inlist[0] > inlist[1]:
        return 512, smallEdge
    elif inlist[0] < inlist[1]:
        return smallEdge, 512
    elif inlist[0] == inlist[1]:
        return 512, 512
    
def GetPathAndResize():
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1): #I'm not familiar with re yet, so I use a C liked way to remove NAME.py
        if current[itera] == '\\':
            dir = current[0: itera]
            break;
    files = os.listdir(dir)#Same reason, remove NAME.py
    for itera in range(len(files)):
        if 'py' in str(files[itera]):
            temp = files[itera]
            files.remove(temp)
            break;
    #print(files)
    outDir = dir + '\\OutputImages\\'
    os.makedirs(outDir)
    #============================================================
    for itera in range(len(files)):
        targetLoc = dir + '\\' + files[itera]
        print(targetLoc)
        target = img.open(targetLoc)
        xEdge, yEdge = reSize(target.size)
        out = target.resize((xEdge, yEdge), img.ANTIALIAS)
        out.save(outDir+ str(itera) +'outImage.png','PNG')
        
        
if __name__ == '__main__':
    GetPathAndResize()

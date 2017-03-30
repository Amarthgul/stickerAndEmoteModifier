import image
import PIL.Image as img
import os

def ImageResize():
    dir = r''#Enter Path here
    stick = '\\'
    files = os.listdir(dir)
    for itera in range(len(files)):
        targetLoc = dir + stick + files[itera]
        print(targetLoc)
        target = img.open(targetLoc)
        xEdge, yEdge = reSize(target.size)
        out = target.resize((xEdge, yEdge), img.ANTIALIAS)
        out.save(r''+ str(itera) +'c.png','PNG')#Output files name

def reSize(inlist):
    smallEdge = int( min(inlist[0], inlist[1]) * 512 / max(inlist[0], inlist[1]))
    if inlist[0] > inlist[1]:
        return 512, smallEdge
    elif inlist[0] < inlist[1]:
        return smallEdge, 512
    elif inlist[0] == inlist[1]:
        return 512, 512
        
        
ImageResize()

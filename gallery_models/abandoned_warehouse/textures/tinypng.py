import os
import os.path
import shutil
from PIL import Image
import tinify

curDirectory = (os.getcwd() + "\\")
curDirectoryList = os.listdir(curDirectory)
curDirPanda = (curDirectory + "panda")
curDirTemp = (curDirectory + "temp")
if not os.path.exists(curDirPanda):
    os.makedirs(curDirPanda)
if not os.path.exists(curDirTemp):
    os.makedirs(curDirTemp)

size = 1024, 1024

tinify.key = "h3qrYHglPqvLbmspJMzYCSMh0xwZM0Hb"

##source = tinify.from_file("P:/TEMP/capas/Capa_CDB - Knack 825 1240.jpg")
##source.to_file("P:/TEMP/capas/Capa_CDB - Knack 825 1240_Processed.jpg")


print("# --------- ----------------------- --------- #")
print("# --------- ----- START CONVERT --- --------- #")
print("# --------- ----------------------- --------- #")


for file in curDirectoryList:
    if os.path.splitext(file)[1].lower() in ('.jpg', '.png'):
        filenameOnly = file[:-4]
        filefull = (curDirectory + file)
        print(filefull)
        filefullOut = (curDirTemp + "\\" + filenameOnly + ".png")
        im = Image.open(filefull)
        rgb_im = im.convert('RGB')
        rgb_im.thumbnail(size, Image.ANTIALIAS)
        rgb_im.save(filefullOut, 'jpeg')
        print(filefullOut + " - Convertido em Jpg")
        source = tinify.from_file(filefullOut)
        filefullOutPanda = (curDirPanda + "\\" + filenameOnly + ".png")
        source.to_file(filefullOutPanda)
        print(filefullOutPanda + " - Otimizado")
        print("-----------------------------------")


print("# --------- ----------------------- --------- #")
print("# --------- - START COPYING SELOS - --------- #")
print("# --------- ----------------------- --------- #")

shutil.rmtree(curDirTemp)

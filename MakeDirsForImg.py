import os
import shutil

#print(os.getcwd())
#print(os.listdir())
#shutil.move(pathFile('003913.jpg'),pathFile('name'))

def pathFile(file):
    return os.path.abspath(str(file))

def countImages():
    images = 0
    for i in os.listdir():
        if '.jpg' in i:
            images += 1
        else:
            continue
    print(images)
    return images

def createFolderForImages():
    countFolders = int(countImages() / 2)
    folderNames = []
    for folderName in range(countFolders):
        os.mkdir(str(folderName))
        folderNames.append(folderName)
    return folderNames


def jpegFounder():
    jpegs = []
    for i in os.listdir():
        if '.jpg' in i:
            jpegs.append(i)
        else:
            continue
    return jpegs




imgCountToFolder = 0
folderCount = 0
for i in os.listdir():
    if '.JPG' in i:
        if imgCountToFolder == 0:
            folder = str(folderCount)
            folderCount += 1
            os.mkdir(folder)
            shutil.move(pathFile(i),pathFile(folder))
            imgCountToFolder += 1
        elif imgCountToFolder == 1:
            shutil.move(pathFile(i),pathFile(folder))
            imgCountToFolder += 1
        if imgCountToFolder == 2:
            imgCountToFolder = 0
    else:
        continue

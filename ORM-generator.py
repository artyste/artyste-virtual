# v0.2

from PIL import Image
import numpy as np
import os

currentDir = os.path.dirname(__file__)
armsAO = os.path.join(currentDir, 'ArmsMat-AO.png')
headAO = os.path.join(currentDir, 'HeadMat-AO.png')
torsoAO = os.path.join(currentDir, 'TorsoMat-AO.png')


def SeekAndGenerate(rootDir):
    print('Start seeking..')
    for d in os.listdir(rootDir):
        if os.path.isdir(os.path.join(rootDir, d)):
            # print(os.path.join(rootDir, d))
            if d.startswith('ArtMonkees'):
                ProcessDir(os.path.join(rootDir, d))


def ProcessDir(dir):
    print('Scanning ' + dir)
    for filename in os.listdir(dir):
        if filename.endswith("-ORM.png"):
            return
    ORM_Dir(dir)


def ORM_Dir(dir):
    print('Generating ORMs for ' + dir)
    for file in os.listdir(dir):
        if file.endswith("-Color.png"):
            # print('Generating: ' + file.replace('-Color', '-ORM'))
            inAO = armsAO if file.find('Arms') > -1 else headAO if file.find('Head') > -1 else torsoAO
            inRO = os.path.join(dir, file).replace('-Color', '-Roughness')
            inME = os.path.join(dir, file).replace('-Color', '-Metallic')
            orm = ORM_Generate(inAO, inRO, inME)
            orm.save(os.path.join(dir, file).replace('-Color', '-ORM'))


def ORM_Generate(inAO, inRO, inME):
    imgAO = Image.open(inAO)
    dataAO = np.asarray(imgAO, dtype='uint16')
    imgRO = Image.open(inRO)
    dataRO = np.asarray(imgRO, dtype='uint16')
    imgME = Image.open(inME)
    dataME = np.asarray(imgME, dtype='uint16')

    r = dataAO.T
    g = dataRO.T
    b = dataME.T
    out_data = np.stack((r.T, g.T, b.T), axis=2).astype('uint8')

    orm = Image.fromarray(out_data)
    return orm


# START
SeekAndGenerate(currentDir)
print('Finish!')

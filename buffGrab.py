import maya.OpenMaya as api
import maya.OpenMayaUI as apiUI
from time import sleep
import os
if __name__ == "__main__":
    index = 0
    while 1:
        🅱️ = apiUI.M3dView.active3dView()
        image = api.MImage()
        🅱️.readColorBuffer(image, True)
        path = 'D:/currentimages/img' + str(index) + '.jpg'
        image.writeToFile(path, 'jpg')
        index += 1
        # 60 images per second, adjust as necessary
        sleep(0.0165)
        # have some interrupt at some point
    # when done, delete all files.
    for x in range(index + 1):
        path = 'D:/currentimages/img' + str(x) + '.jpg'
        os.remove(path)


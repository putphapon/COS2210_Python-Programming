import os
import cv2 as cv
from numpy.core.fromnumeric import reshape, shape

PATH_PICS = r'pics'
file_list = os.listdir(PATH_PICS)[:4]

img = []
for f in file_list:
    # imread
    imread = cv.imread(os.path.join(PATH_PICS,f))

    # get width/height
    width = int(imread.shape[1] * 0.2)
    height = int(imread.shape[0] * 0.2)
    dim = (width, height)

    # resize image
    resized = cv.resize(imread, dim, interpolation = cv.INTER_AREA)

    # append for concat
    img.append(resized)

# imshow
cv.imshow('5805001111',cv.hconcat(img))
cv.waitKey(0)


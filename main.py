import cv2 as cv
import numpy as np

import lun
import sacn

if __name__ == '__main__':
    sacn.videox()
    src = cv.imread('E:\Python\lunkuo\img.png')
    ld = lun.ShapeAnalysis()
    ld.analysis(src)
    cv.waitKey()

import json
import cv2
import numpy as np
import sys
import time



img = cv2.imread('./Hopper1.bmp') #image read

start_time = time.clock()

width = len(img[0])
height = sum([len(arr) for arr in img])/width
region1 = img[5*height/16:14*height/16, 0:width]


img_str = cv2.imencode('.bmp', region1)[1].tostring()
print len(img_str)
img_str = img_str[0:518453]
print len(img_str)


nparr = np.fromstring(img_str, np.uint8)
img2 = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
print("--- %s seconds ---" % (time.clock() - start_time))
print type(img_str)

cv2.imwrite('/Users/harshayugirase/Desktop/XDtest.bmp', img2)






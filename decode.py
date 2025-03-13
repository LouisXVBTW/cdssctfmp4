import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import csv
import time

import cv2
vidcap = cv2.VideoCapture('output.mp4')
success,image = vidcap.read()
countFrame = 0
while success:
  cv2.imwrite("out-img/frame%d.jpg" % countFrame, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  countFrame += 1
binary = []
for i in range(0,countFrame):
    fname = 'frame'+str(i)+'.jpg'
    img=mpimg.imread('out-img/frame0.jpg')
    print(type(img))
    print(img.flatten())

    

    
    tmp = []
    count = 0
    for i in img.flatten():
        if count%12 == 0:
            #print (len(tmp))
            #print(tmp)
            #print ("NEXT!!")
            
            #time.sleep(0.5)
            if 5 <= sum(tmp) <= 150:
                binary.append(1)
            if 160 <= sum(tmp) <= 3060:
                binary.append(0)
            tmp = []
        tmp.append(int(str(i)))
        count += 1

    #with open('output1.txt', 'wb') as f:
    #    csv.writer(f).writerow(binary)
print (type(binary))

binary_str = "".join(map(str, binary))
byte_array = bytearray(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))

with open("output2", "wb") as f:
    f.write(byte_array)
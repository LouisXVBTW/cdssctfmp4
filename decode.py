import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import csv
import time
img=mpimg.imread('out-img/frame0.jpg')
print(type(img))
print(img.flatten())

with open('decoded', 'w') as f:
    csv.writer(f).writerow(img.flatten())

binary = []
tmp = []
count = 0
for i in img.flatten():
    if count%12 == 0:
        #print (len(tmp))
        #print(tmp)
        #print ("NEXT!!")
        
        #time.sleep(0.5)
        if 5 <= sum(tmp) <= 150:
            binary.append(0)
        if 160 <= sum(tmp) <= 3060:
            binary.append(1)
        tmp = []
    tmp.append(int(str(i)))
    count += 1

with open('output.txt', 'w') as f:
    csv.writer(f).writerow(binary)


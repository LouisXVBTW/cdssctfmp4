import cv2
vidcap = cv2.VideoCapture('output.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("out-img/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

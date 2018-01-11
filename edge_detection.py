import cv2
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import imutils

stitcher = cv2.createStitcher(False)


mypath="path to file"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]))
  #oonvert to black and white
  gray_image = cv2.cvtColor(images[n], cv2.COLOR_BGR2GRAY)

  #thresholding
  th = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

  #find contours
  im2,contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  cv2.drawContours(images[n], contours, -1, (0, 255, 0), 3)
  #cv2.imshow('image',images[n])
  #result=stitcher.stitch(images[n])

  cv2.imshow('image',images[n])
  cv2.waitKey(0)

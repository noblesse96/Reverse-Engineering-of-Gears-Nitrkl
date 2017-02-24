import cv2
import numpy as np

gearimage  = cv2.imread('gearcount_01.png');

cv2.imshow('Initial Image' , gearimage)

gearGray = cv2.cvtColor(gearimage, cv2.COLOR_BGR2GRAY );

gearBlur = cv2.blur(gearGray, (4, 4 ));

gearThresh = cv2.threshold(gearThresh, 105, 255 , cv2.THRESH_BINARY)

gearThresh = gearThresh[1]

cv2.imshow('After Threshold', gearThresh)

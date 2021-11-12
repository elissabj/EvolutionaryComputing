#Fractals
#Elisa Ramos Gomez
#Last modification: 13 oct 2021 12:55 

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import math


def lines(img, x0, y0, l, angle, setcolor):
  x1 = x0-(l*math.cos(angle/57.29578))
  y1 = y0-(l*math.sin(angle/57.29578))

  point0 = ( int(x0), int(y0) )
  point1 = ( int(x1), int(y1) )
  cv2.line(img, point0, point1, setcolor, 9)
  return x1, y1


def draw(img, x0, y0, l, angle, ind, setcolor):
  if ind > 0:
    x1, y1 = lines(img, x0, y0, l, angle, setcolor)
    draw(img, x1, y1, l/1.2, angle+w1, ind-1, setcolor)
    draw(img, x1, y1, l/1.55, angle+w2, ind-1, setcolor)
    draw(img, x1, y1, l/1.8, angle+w3, ind-1, setcolor)


def draw2(img, x0, y0, l, angle, ind, setcolor):
  if ind > 0:
    x1, y1 = lines(img, x0, y0, l, angle, setcolor)
    draw2(img, x0,y0, l-1, angle-10, ind-1, setcolor)



img = np.zeros((500, 500, 3), dtype="uint8")
img[:255] = (224,150,68)

img[255:258] = (191,127,2) 
img[258:263] = (183,118,10) 
img[263:345] = (173,107,2) 

img[345:370]=(229,234,233) 
img[370:]=(176,209,253) 


#Clouds
color=(238, 238, 238)
w1=238
w2=273
w3=144
draw(img,100,80,37,28,9, color)
draw(img,100,100,37,153,7, color)

draw(img,265,70,37,-136,6, color)

draw(img,450,70,37,-120,9, color)
draw(img,450,110,37,47,7, color)


#Bushes

color=(77, 170, 24)
w1=8
draw(img,105,489,43,-17,7, color)

w1=-15
w2=352
draw(img,430,570,43,105,8, color)
draw(img,427,570,50,125,8, color)
draw(img,472,490,47,-17,9, color)


#Waves

color= (218,136,14)
w1=6
w2=172
w3=1
w0=173


draw(img,0,325,13,w0,7, color)
draw(img,70,327,13,w0-3,7, color)
draw(img,140,325,13,w0,7, color)
draw(img,200,327,13,w0-3,7, color)
draw(img,270,325,13,w0,7, color)
draw(img,350,327,13,w0-3,7, color)
draw(img,420,325,13,w0,7, color)
draw(img,490,327,13,w0-3,7, color)


draw(img,0,300,13,w0,7, color)
draw(img,70,302,13,w0-3,7, color)
draw(img,140,300,13,w0,7, color)
draw(img,200,302,13,w0-3,7, color)
draw(img,270,300,13,w0,7, color)
draw(img,350,302,13,w0-3,7, color)
draw(img,420,300,13,w0,7, color)
draw(img,490,302,13,w0-3,7, color)


draw(img,0,275,13,w0,7, color)
draw(img,70,277,13,w0-3,7, color)
draw(img,140,275,13,w0,7, color)
draw(img,200,277,13,w0-3,7, color)
draw(img,270,275,13,w0,7, color)
draw(img,350,277,13,w0-3,7, color)
draw(img,420,275,13,w0,7, color)
draw(img,490,277,13,w0-3,7, color)


color= (229,234,233)
w1=6
w2=172
w3=1
w0=173


draw(img,0,350,13,w0,7, color)
draw(img,70,352,13,w0-3,7, color)
draw(img,140,350,13,w0,7, color)
draw(img,200,352,13,w0-3,7, color)
draw(img,270,350,13,w0,7, color)
draw(img,350,352,13,w0-3,7, color)
draw(img,420,350,13,w0,7, color)
draw(img,490,352,13,w0-3,7, color)


draw(img,0,365,13,w0,7, color)
draw(img,70,367,13,w0-3,7, color)
draw(img,140,365,13,w0,7, color)
draw(img,200,367,13,w0-3,7, color)
draw(img,270,365,13,w0,7, color)
draw(img,350,367,13,w0-3,7, color)
draw(img,420,365,13,w0,7, color)
draw(img,490,367,13,w0-3,7, color)


#butterflies
color=(59, 59, 59)
draw2(img,370,370,25,-10,10, color)
draw2(img,370,370,25,160,10, color)

color=(3, 102, 255)
draw2(img,350,330,25,-10,10, color)
draw2(img,350,330,25,160,10, color)


cv2_imshow(img)

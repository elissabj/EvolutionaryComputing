#2ndOrderPractice9
#Author: Elisa Ramos GOmez
#Rule: W110 and W110R with |N| = 5
#Last modification: 21 Nov, 2021

import cv2
import numpy as np
from IPython import display as display
import ipywidgets as ipw
import PIL
from io import BytesIO
from random import random

N=100

cells0=N*[0]
cells1=N*[0]
cells2=N*[0]

#Setup inicial 
for i in range(N):
  cells1[i]= 0 if random()>0.5 else 1                       #random config
  #cells1[i]=1 if i == N/2 else 0                           #only one cell
 


rule = {"00001", "00010", "00011", "00101", "00110"}        #set of rules that have 1.


def apply_rule(left,leftM,center,right,rightM):

  global rule
  numberStr = str(leftM) + str(left) + str(center) + str(right) + str(rightM)

  return 1 if numberStr in rule else 0                      #consulting if the str exist in the set 


def iteration():
  global cells0,cells1,N

  for i in range(2,N-2):
    cells0[i]=apply_rule(cells1[i-1],cells1[i-2],cells1[i],cells1[i+1],cells1[i+2])
  
  cells1[:]=cells0[:]


def iteration2nd():
  global cells0,cells1,cells2,N

  for i in range(2,N-2):
    cells0[i]=apply_rule(cells1[i-1],cells1[i-2],cells1[i],cells1[i+1],cells1[i+2])
    cells0[i]= 0 if cells0[i]==cells2[i] else 1

  cells2[:]=cells1[:]  
  cells1[:]=cells0[:]


x0=0
y0=0
maxX=500
maxY=500
color=(255,255,255)
margin=1
stride = (maxX - 2*margin)/N


def graph_cells(img,cells):
  global x0,y0,maxX,maxY,margin,color,stride,N
  r=5
  for i in range(N):
    if cells[i]:
      start=(int(x0+stride*i+margin),int(y0+margin))
      end=(int(x0+stride*(i+1)-margin), int(y0+stride-margin))
      cv2.rectangle(img,start,end,color,-1)


wIm = ipw.Image()
display.display(wIm)

img = np.zeros((500, 500, 3), dtype="uint8")

graph_cells(img,cells1)
y0+=stride

while y0<=maxY:
  iteration()                                              #normal     Wxxx
  #iteration2nd()                                          #2ndOrder WxxxR
  graph_cells(img,cells0)
  y0+=stride

pilIm = PIL.Image.fromarray(img, mode="RGB")
with BytesIO() as fOut:
    pilIm.save(fOut, format="png")
    byPng = fOut.getvalue()
      
# set the png bytes as the image value; 
# this updates the image in the browser.
wIm.value=byPng
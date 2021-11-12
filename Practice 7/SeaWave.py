#Practice7
#Elisa Ramos Gomez
#Last modified 28/oct/2021

import PIL
import cv2
import time
import numpy as np
from io import BytesIO
import ipywidgets as ipw
from IPython import display as display


N=20
particles = np.zeros((N,N))
up= np.ones((N,N))

wIm = ipw.Image()
display.display(wIm)

r = 1
maxX=500
maxY=500
x0=100
y0=100

def graph_particles(img):
  global particles,x0,y0,maxX,maxY,N, rad
  stride = (maxX - 2*x0)/N 
 
  for i in range(20):
    for j in range(20):
      cv2.circle(img,(int(x0+stride*i),int(y0+stride*j)),int(particles[i][j]),(255,255,255),-1)
    


def iteration():
  global particles, r

  #influence of neighbors
  for i in range(N):
    for j in range(N):
      if up[i][j] ==1:
        #up 
        if j > 0:
          particles[i][j] += 0.5*particles[i][j-1]
        else:
          particles[i][j] += 0.5*particles[i][0]
        #down
        if j < N-1:
          particles[i][j] += 0.5*particles[i][j+1]
        else:
          particles[i][j] += 0.5*particles[i][N-1]

        #left
        if i > 0:
          particles[i][j] += 0.5*particles[i-1][j]
        else:
          particles[i][j] += 0.5*particles[i][0]
        #right
        if i < N-1:
          particles[i][j] += 0.5*particles[i+1][j]
        else:
          particles[i][j] += 0.5*particles[N-1][j]
       
      
      if up[i][j]==1 and particles[i][j]>=5:
        up[i][j]=0
        particles[i][j] = 1
      
      if up[i][j]==0 and particles[i][j]<=1:
        up[i][j]=1
        particles[i][j] = 1



    #decay
    particles[i][j]*=0.9

    
  
img = np.zeros((500, 500, 3), dtype="uint8")
particles[9][9]=10
graph_particles(img)

for i in range(100):
  iteration()
  img[:]=(0,0,0)
  time.sleep(0.3)

  graph_particles(img)
  pilIm = PIL.Image.fromarray(img, mode="RGB")
  with BytesIO() as fOut:
      pilIm.save(fOut, format="png")
      byPng = fOut.getvalue()
        
  # set the png bytes as the image value
  # this updates the image in the browser.
  wIm.value=byPng  

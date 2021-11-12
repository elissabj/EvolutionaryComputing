#Practice7
#Elisa Ramos Gomez
#Last modified 28/oct/2021

import cv2
import PIL
import math as m
import numpy as np
import random as rd
from io import BytesIO
import ipywidgets as ipw
from IPython import display as display


class Particle:
  MaxV = np.sqrt(2)

  def __init__(self,x,y,vx,vy,WallParticle=False):
    self.r = np.array([float(x),float(y)])
    self.v = np.array([float(vx),float(vy)])
    self.WallParticle=WallParticle
    self.F=np.array([0.0,0.0])

  def getX(self):
    return self.r[0]

  def getY(self):
    return self.r[1]

  def normalize_vector(self,x):
    norm=np.linalg.norm(x)
    if norm==0:
      return x*np.inf
    return x/norm


  def r12(self,r2):
    return np.linalg.norm(r2-self.r)


  def calculateF(self,r2):
    if self.WallParticle==True:
      return np.array([0.,0.])
      
    r12=self.r-r2
    r12magnitude=np.linalg.norm(r12)
    if r12magnitude<=2: #si estamos en contacto
      return self.normalize_vector(r12)/ (r12magnitude**2)

    return np.array([0.,0.])


  def update_r(self):
    if self.WallParticle==True:
      return
    self.r+=self.v
    return
  
  def update_r2(self):
    if self.WallParticle==True:
      return
    self.r-=self.v
    return


  def update_v(self):
    if self.WallParticle==True:
      return
    self.v+=self.F

    vmag=np.linalg.norm(self.v)

    if vmag> self.MaxV: #no queremos que tengan velocidades muy grande
      self.v=self.normalize_vector(self.v)*self.MaxV
    return

  def update_v2(self):
    if self.WallParticle==True:
      return
    self.v-=self.F

    vmag=np.linalg.norm(self.v)

    if vmag> self.MaxV: #no queremos que tengan velocidades muy grande
      self.v -= self.normalize_vector(self.v)*self.MaxV
    return
    


  def graph(self,x0,y0,img):
    if self.WallParticle==True:
      color=(0,255,255)
      cv2.rectangle(img, (int(x0+self.r[0]+5),int(y0-self.r[1]-5)) , (int(x0+self.r[0]-5),int(y0-self.r[1]+5)) ,color,-1)
    else:
      color=(255,255,255)
      cv2.circle(img,(int(x0+self.r[0]),int(y0-self.r[1])),10,color,-1)
    return

particles=[]
lines = set()

def lineOfWallParticles(x1,y1,x2,y2,N):
  global particles, lines
  x=np.linspace(x1,x2,N)
  y=np.linspace(y1,y2,N)
  for i in range(N):
    particles.append(Particle(x[i],y[i],0,0,WallParticle=True))

def moveBr (x1,y1,x2,y2):
  slope = 2 * (y2-y1)
  curr_slope = slope - (x2 - x1)

  itX = x1
  itY = y1

  while itX <= x2:
    aux = (itX, itY)
    aux2= (itY, itX)
    lines.add(aux)

    if curr_slope >= 0:
      itY += 1
      curr_slope -= 2 * (x2-x1)
    
    curr_slope += slope
    itX+= 1


def Bresenham (x1,y1,x2,y2):
  if x1 > x2:
    Bresenham(x2,y2,x1,y1)
    return
  
  sdx = x2-x1
  sdy = y2-y1

  if sdy >= 0:
    if sdx >= sdy:
      moveBr(x1,y1,x2,y2)
    else:
      x1,y1,x2,y2 = x2,y2,x1,y1
      moveBr(x1,y1,x2,y2)
  else:
    if sdx >= -sdy:
      y1 = -y1
      y2 = -y2
      moveBr(x1,y1,x2,y2)
    else:
      y1 = -y1
      y2 = -y2
      x1,y1,x2,y2 = x2,y2,x1,y1
      moveBr(x1,y1,x2,y2)



wIm = ipw.Image()
display.display(wIm)


maxX=500
maxY=500
x0=int(maxX/2)
y0=int(maxY/2)

  
img = np.zeros((500, 500, 3), dtype="uint8")
boxImg = np.zeros((500, 500, 3), dtype="uint8")


lineOfWallParticles(-50,50,70,50,20)


lineOfWallParticles(-100,100,30,100,20)
Bresenham(-100,100,30,100)

lineOfWallParticles(-100,-100,100,-100,20)
Bresenham(-100,-100,100,-100)


lineOfWallParticles(-100,100,-100,-100,20)

for i in range (-100, 100):
  Bresenham(-100, i, -100, i)


lineOfWallParticles(100,-100,100,100,20)
for i in range (-100, 100):
  Bresenham(100, i, 100, i)


K = 20
for i in range (K):
  particles.append(Particle(rd.randrange(-90,90),rd.randrange(-90,90), rd.random(), rd.random(), WallParticle=False))


MaxIterations = 1000

NumParticles=len(particles)

boxImg[:]=(0,0,0)
for p in particles:
  if (p.WallParticle):
    p.graph(x0,y0,boxImg)

for count in range(MaxIterations):
  img[:] = boxImg

  for i in range(NumParticles):
    for j in range(NumParticles):
      if i!=j:
          Fij=particles[i].calculateF(particles[j].r)
          particles[i].F+= Fij
    

  for p in particles:
    if p.WallParticle == False:
      x = int(p.getX())
      y = int(p.getY())
      aux = (x,y)
      if aux not in lines:
        p.update_v()
        p.update_r()
      else:
        p.update_v2()
        p.update_r2()

      p.graph(x0,y0,img)
      p.F[:]=0
      
      
  
  cv2.putText( img,str(count),(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
  
  pilIm = PIL.Image.fromarray(img, mode="RGB")
  with BytesIO() as fOut:
      pilIm.save(fOut, format="png")
      byPng = fOut.getvalue()
        
  # set the png bytes as the image value; 
  # this updates the image in the browser.
  wIm.value=byPng

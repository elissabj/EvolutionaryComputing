## Self-Organizing Maps by Paras Chopra
## www.paraschopra.com
## paras1987@gmail.com
##
## Please give credit if you use my work.

from random import *
from math import *

class Node:

    def __init__(self, FV_size=10, PV_size=10, Y=0, X=0):
        self.FV_size=FV_size
        self.PV_size=PV_size
        self.FV = [0.0]*FV_size # Feature Vector weights 
        self.PV = [0.0]*PV_size # Prediction Vector etiqueta 
        self.X=X # X location
        self.Y=Y # Y location
        
        for i in range(FV_size):
            self.FV[i]=random() # Assign a random number from 0 to 1
            
        for i in range(PV_size):
            self.PV[i]=random() # Assign a random number from 0 to 1


class SOM:

    #Let radius=False if you want to autocalculate the radis
                  #sizes of grid, FV_size means de dimensions 
    def __init__(self, height=10, width=10, FV_size=10, PV_size=10, radius=False, learning_rate=0.005):
        self.height=height
        self.width=width
        self.radius=radius if radius else (height+width)/2
        self.total=height*width   #total number of nodes
        self.learning_rate=learning_rate
        self.nodes=[0]*(self.total)   #as an array of nodes for total nodes
        self.FV_size=FV_size
        self.PV_size=PV_size
        for i in range(self.height):
            for j in range(self.width):
                self.nodes[(i)*(self.width)+j]=Node(FV_size, PV_size,i,j)

    # Train_vector format: [ [FV[0], PV[0]],
    #                        [FV[1], PV[1]], so on..
    # have inerce and influence for this training
    #this function decaying with respect the time pass
    #iterations defaul value 1000
    def train(self, iterations=500, train_vector=[[[0.0],[0.0]]]):
        time_constant=iterations/log(self.radius)
        radius_decaying=0.0
        learning_rate_decaying=0.0
        influence=0.0
        stack=[] #Stack for storing best matching unit's index and updated FV and PV
        temp_FV=[0.0]*self.FV_size
        temp_PV=[0.0]*self.PV_size
        for i in range(1,iterations+1):
            #print "Iteration number:",i
            radius_decaying=self.radius*exp(-1.0*i/time_constant)
                                    #as exponenticial
            learning_rate_decaying=self.learning_rate*exp(-1.0*i/time_constant)
            ##print (i, end=', ')  #know with iterations
            ##if i%50==0:
              ##print("")
            
            for  j in range(len(train_vector)):
                input_FV=train_vector[j][0]
                input_PV=train_vector[j][1]
                best=self.best_match(input_FV)
                stack=[]
                for k in range(self.total):
                    dist=self.distance(self.nodes[best],self.nodes[k])
                    if dist < radius_decaying:
                        temp_FV=[0.0]*self.FV_size
                        temp_PV=[0.0]*self.PV_size
                        influence=exp((-1.0*(dist**2))/(2*radius_decaying*i))

                        for l in range(self.FV_size):
                            #Learning
                            temp_FV[l]=self.nodes[k].FV[l]+influence*learning_rate_decaying*(input_FV[l]-self.nodes[k].FV[l])

                        for l in range(self.PV_size):
                            #Learning
                            temp_PV[l]=self.nodes[k].PV[l]+influence*learning_rate_decaying*(input_PV[l]-self.nodes[k].PV[l])

                        #Push the unit onto stack to update in next interval
                        stack[0:0]=[[[k],temp_FV,temp_PV]]

                
                for l in range(len(stack)):
                    
                    self.nodes[stack[l][0][0]].FV[:]=stack[l][1][:]
                    self.nodes[stack[l][0][0]].PV[:]=stack[l][2][:]

                
                                    

                

    #Returns prediction vector
    def predict(self, FV=[0.0],get_ij=False):
        best=self.best_match(FV)
        if get_ij:
          return self.nodes[best].PV,self.nodes[best].X,self.nodes[best].Y
        return self.nodes[best].PV
        
    #Returns best matching unit's index BMU
    #iterate all nodes 
    def best_match(self, target_FV=[0.0]):

        minimum=sqrt(self.FV_size) #Minimum distance
        minimum_index=1 #Minimum distance unit
        temp=0.0
        for i in range(self.total):
            temp=0.0
            temp=self.FV_distance(self.nodes[i].FV,target_FV)
            if temp<minimum:
                minimum=temp
                minimum_index=i

        
        return minimum_index  #return where is the BMU



    #euclidian distance didnt knows priori so made an iterations
    def FV_distance(self, FV_1=[0.0], FV_2=[0.0]):
        temp=0.0
        for j in range(self.FV_size):
                temp=temp+(FV_1[j]-FV_2[j])**2

        temp=sqrt(temp)
        return temp
    #euclidian distance 
    def distance(self, node1, node2):
        return sqrt((node1.X-node2.X)**2+(node1.Y-node2.Y)**2)


#Practice 8
#Elisa Ramos Gomez
#Last modified 12/nov/2021
import csv 

N = 20
trainingV = []
tagCountry = []
countryName = []
totalCountries = 40
parameters = [[], [], [], [], [], [], [], [], [], []]


def countriesPrint(countries):
    results = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append("   ")
        results.append(row)

    for i, j in countries.keys():
        results[i][j] = countries[(i, j)]    

    #Print map
    for i in range(N):
        print(f"{results[i]}")



with open('Data.csv', mode='r') as csvFile:
#with open('Data2.csv', mode='r') as csvFile:    #to open other file

    csvReader = csv.DictReader(csvFile)
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            lineCount += 1
       
        currValue = row["2014 [YR2014]"]
        currCountryCode = row["país Code"]
        if len(currValue) != 0:
          parameters[(lineCount - 1) % 10].append(float(row["2014 [YR2014]"]))
          
          if not currCountryCode in tagCountry:
            tagCountry.append(currCountryCode)
            countryName.append(currCountryCode)
          lineCount += 1
        

tagCountry = set(tagCountry)

for i in range(10):
    maxValue = max(parameters[i])
    for j in range(totalCountries):
        parameters[i][j] /= maxValue


for i in range(totalCountries):
    row = []
    for j in range(10):
        row.append(parameters[j][i])
    trainingV.append([row, [i]])


a = SOM(20, 20, 10, 1, False, 0.03)

print("Training...")
a.train(1000, trainingV)

positions = {}

#Get BMU 
for K in range(totalCountries):
    currCountry = trainingV[K][0]
    value, i, j = a.predict(currCountry, True)
    positions[(i, j)] = countryName[K]


print(totalCountries,"countries in the SOM.")
countriesPrint(positions)
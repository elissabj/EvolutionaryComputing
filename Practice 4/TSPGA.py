#Practice4
#Example of Genetic Algorithm
#TSP Problem
#Elisa Ramos Gomez
#Last modified 9/oct/2021

import math
import random
import time
import sys
import matplotlib.pyplot as plt
import numpy as np
from IPython import display as display
from functools import cmp_to_key
import ipywidgets as widgets


def nextPermutation(lista : list):
    
    nums = lista.copy()

    found = False
    i = len(nums)-2
    while i >=0:
        if nums[i] < nums[i+1]:
            found =True
            break
        i-=1
    if not found:
         nums.sort()
    else:
        m = findMaxIndex(i+1,nums,nums[i])
        nums[i],nums[m] = nums[m],nums[i]
        nums[i+1:] = nums[i+1:][::-1]
    return nums

def findMaxIndex(index,a,curr):
    ans = -1
    index = 0
    for i in range(index,len(a)):
        if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
    return index


listPossibleChromosomes = []
possibleChromosome = [0,1,2,3,4,5,6]
listPossibleChromosomes.append(possibleChromosome)


for i in range(1,5041):
    chromosome = nextPermutation(listPossibleChromosomes[i-1])
    listPossibleChromosomes.append(chromosome)


def create_button():
  button = widgets.Button(
    description='Next Generation',
    disabled=False,
    button_style='', 
    tooltip='Next Generation',
    icon='check' 
  )
  return button


#graph cities with weight in air distance miles
cities = [[0,2318,0,0,6663,0,2094], 
          [2318,0,0,3422,0,2539,0],
          [0,0,0,0,1474,6240,4281],
          [0,3422,0,0,0,5558,3624],
          [6663,0,1474,0,0,5871,0],
          [0,2539,6240,5558,5871,0,0],
          [2094,0,4281,3624,0,0,0]]


N_chromosomes = 200

#probability of mutation
prob_m=0.5


F0 = []
fitness_values=[]

def random_chromosome():
    pos = random.randrange(0,5012)
    return pos
      


for i in range(0,N_chromosomes):
    F0.append(listPossibleChromosomes[random_chromosome()])
    fitness_values.append(0)


def f(x):
    distancePath = 0
    for i in range (0,len(x)-1):
      if cities[x[i]][x[i+1]] != 0:
        distancePath += cities[x[i]][x[i+1]]
      else:
        distancePath = 1e9+i  
        break
    return distancePath


def evaluate_chromosomes():
    global F0
    for p in range(N_chromosomes):
        fitness_values[p]=f(F0[p])



def compare_chromosomes(chromosome1,chromosome2):

    fvc1=f(chromosome1)
    fvc2=f(chromosome2)

    if fvc1 > fvc2:
    # if fvc1 < fvc2: # maximizar
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


def PMXCrossover(parent1, parent2):

    firstCrossPoint = random.randint(0,len(parent1)-2)
    secondCrossPoint = random.randint(firstCrossPoint+1,len(parent1)-1)
    
    parent1MiddleCross = parent1[firstCrossPoint:secondCrossPoint]
    parent2MiddleCross = parent2[firstCrossPoint:secondCrossPoint]


    temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]
    temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]

    relations = []
    for i in range(len(parent1MiddleCross)):
        relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])

    def recursion1 (temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross) :
        child = list([0 for i in range(len(parent1))])
        for i,j in enumerate(temp_child[:firstCrossPoint]):
            c=0
            for x in relations:
                if j == x[0]:
                    child[i]=x[1]
                    c=1
                    break
            if c==0:
                child[i]=j
        j=0
        for i in range(firstCrossPoint,secondCrossPoint):
            child[i]=parent2MiddleCross[j]
            j+=1

        for i,j in enumerate(temp_child[secondCrossPoint:]):
            c=0
            for x in relations:
                if j == x[0]:
                    child[i+secondCrossPoint]=x[1]
                    c=1
                    break
            if c==0:
                child[i+secondCrossPoint]=j
        child_unique=np.unique(child)
        if len(child)>len(child_unique):
            child=recursion1(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        return(child)

    def recursion2(temp_child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross):
        child = list([0 for i in range(len(parent1))])
        for i,j in enumerate(temp_child[:firstCrossPoint]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i]=x[0]
                    c=1
                    break
            if c==0:
                child[i]=j
        j=0
        for i in range(firstCrossPoint,secondCrossPoint):
            child[i]=parent1MiddleCross[j]
            j+=1

        for i,j in enumerate(temp_child[secondCrossPoint:]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i+secondCrossPoint]=x[0]
                    c=1
                    break
            if c==0:
                child[i+secondCrossPoint]=j
        child_unique=np.unique(child)
        if len(child)>len(child_unique):
            child=recursion2(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        return(child)

    child1=recursion1(temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
    child2=recursion2(temp_child2,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
    return child1, child2


suma=float(N_chromosomes*(N_chromosomes+1))/2.
Lwheel=N_chromosomes*10




def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    if acc==0:
      return [0]*Lwheel
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
##    print fraction
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
##    print fraction

    wheel=[]
    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
            

F1=F0[:]
n=0

def nextgeneration(b):
    global n
    display.clear_output(wait=True)
    display.display(button)
    F0.sort(key=cmp_to_key(compare_chromosomes) )
    #print(F0)
    #print(fitness_values)
    print( "Best solution so far:")
    n+=1
    print( n,F0[0],"\nf(",F0[0],")= ", f(F0[0]) )
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    roulette=create_wheel()

    for i in range(0,int((N_chromosomes-2)/2)):      
        #Two parents are selected

        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated

        off = PMXCrossover(F0[p1], F0[p2])
        o1 = off[0]
        o2 = off[1]

        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            pos = random.randrange(0,7)
            pos2 =  random.randrange(0,7)
            o1[pos],o1[pos2] = o1[pos2], o1[pos]
        if random.random() < prob_m:
            pos = random.randrange(0,7)
            pos2 =  random.randrange(0,7)
            o2[pos],o2[pos2] = o2[pos2], o2[pos]
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    # graph_population(F1)
    #The generation replaces the old one
    F0[:]=F1[:]
    evaluate_chromosomes()


button=create_button()
button.on_click(nextgeneration)
display.display(button)


F0.sort(  key=cmp_to_key(compare_chromosomes))
evaluate_chromosomes()
#Practice4
#Example of Genetic Algorithm 
#Knapsack
#Elisa Ramos Gomez
#Last modified 7/oct/2021


w=[] #weights floats 
v=[] #values 1 100 integers
W = 1  


import ipywidgets as widgets

def create_button():
  button = widgets.Button(
    description='Next Generation',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Next Generation',
    icon='check' # (FontAwesome names without the `fa-` prefix)
  )
  return button

import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from functools import cmp_to_key
from IPython import display as display


#Make 20 values in integers and save it
for i in range (0, 20):
    v.append(random.randrange(1,101))


#Make 20 weights in floats and save it
for i in range (0, 20):
    w.append(random.random())

print(v)
print(w)

#Chromosomes are 4 bits long
L_chromosome= len(v)

#Number of chromosomes
N_chromosomes=40
#probability of mutation
prob_m=0.5

crossover_point=int(L_chromosome/2)


def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.5:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome


F0=[]
fitness_values=[]

for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)


def decode_chromosome(chromosome):
  global L_chromosome,v,w

  Total_weight = sum([w_i*c_i for w_i,c_i in zip(w,chromosome)])
  Total_value = sum([v_i*c_i for v_i,c_i in zip(v,chromosome)])

  return int(Total_value),int(Total_weight)


def f(x):
  global W
  Total_value,Total_weight=x
  excess = Total_weight-W
  return Total_value if excess <= 0 else Total_value - 100000* excess 

        
def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v=decode_chromosome(F0[p])
        fitness_values[p]=f(v)


def compare_chromosomes(chromosome1,chromosome2):
    vc1=decode_chromosome(chromosome1)
    vc2=decode_chromosome(chromosome2)
    fvc1=f(vc1)
    fvc2=f(vc2)
    # if fvc1 > fvc2:
    if fvc1 < fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


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

    print( "Best solution so far:")
    n+=1
    print( n,F0[0],"\nf(",decode_chromosome(F0[0]),")= ", f(decode_chromosome(F0[0])) )
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    roulette=create_wheel()
    
    for i in range(0,int((N_chromosomes-2)/2)):      
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
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

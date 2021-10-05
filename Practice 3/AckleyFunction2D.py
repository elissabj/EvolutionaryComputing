#Ackley function 2D
#Example of Genetic Algorithm
#Elisa Ramos Gomez
#Last modified 3/oct/2021


from numpy import sqrt
from numpy import exp
from numpy import cos
from numpy import pi
from numpy import e
import random


from IPython import display as display
from functools import cmp_to_key
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


#Chromosomes are 4 bits long
L_chromosome=4
N_chains=2**L_chromosome


#Lower and upper limits of search space
a=-0.5
b=1
crossover_point=int(L_chromosome/2)


#Made one chromosome in 2D
def random_chromosome():
    chromosome = []
    
    x_chromosome=[]
    y_chromosome=[]
    x = 0
    y = 0
    for i in range(0, L_chromosome):
        if random.random()<0.5:
          x = 0
        else:
          x = 1
        if random.random()<0.5:
          y = 0
        else:
          y = 1

        x_chromosome.append(x)
        y_chromosome.append(y)
      
    
    chromosome.append([x_chromosome,y_chromosome])
    
    return chromosome


#Number of chromosomes
N_chromosomes=20


#probability of mutation
prob_m=0.15


F0=[]
fitness_values=[]


for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)



#binary codification
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    for p in range(L_chromosome):
        value+=(2**p)*chromosome[-1-p]

    return a+(b-a)*float(value)/(N_chains-1)



def f(x,y):
    #Ackley function 2D
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * pi * x)+cos(2 * pi * y))) + e + 20
    


def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        listAux = F0[p]
        xVal = listAux[0][0]
        yVal = listAux[0][1]
        x_val_decode = decode_chromosome(xVal)
        y_val_decode = decode_chromosome(yVal)

        fitness_values[p]=f(x_val_decode, y_val_decode)


def compare_chromosomes(chromosome1,chromosome2):
    x1_val = chromosome1[0][0]
    y1_val = chromosome1[0][1]

    x2_val = chromosome2[0][0]
    y2_val = chromosome2[0][1]

    x_vc1=decode_chromosome(x1_val)
    y_vc1=decode_chromosome(y1_val)

    x_vc2=decode_chromosome(x2_val)
    y_vc2=decode_chromosome(y2_val)

    fvc1=f(x_vc1,y_vc1)
    fvc2=f(x_vc2,y_vc2)

    if fvc1 > fvc2:
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
        Np = int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
        

F1=F0[:]
n = 0


def nextgeneration(b):
    global n
    display.clear_output(wait=True)
    display.display(button)

    F0.sort(key=cmp_to_key(compare_chromosomes))
    print( "Best solution so far:")
    
    n += 1
    auxList = F0[0]
    print( n,  "f(",decode_chromosome(auxList[0][0]),",",decode_chromosome(auxList[0][1]), ")= ", f(decode_chromosome(auxList[0][0]),decode_chromosome(auxList[0][1])) )


    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]

    for i in range(0,int((N_chromosomes-2)/2)):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated o de offspring de progenea(: 
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            auxO1 = o1[0][0]
            aux2O1 = o1[0][1]
            auxO1[int(round(random.random()*(L_chromosome-1)))]^=1
            aux2O1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            auxO2 = o2[0][0]
            aux2O2 = o2[0][1]
            auxO2[int(round(random.random()*(L_chromosome-1)))]^=1
            aux2O2[int(round(random.random()*(L_chromosome-1)))]^=1

        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    #The generation replaces the old one
    F0[:]=F1[:]


button=create_button()
button.on_click(nextgeneration)
display.display(button)
evaluate_chromosomes()

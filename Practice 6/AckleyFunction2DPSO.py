#Ackley function 2D
#Example of PSO based on the wikipedia entry
#Elisa Ramos Gomez
#Last modification: 18 oct 2021 18:55 

from numpy import sqrt
from numpy import exp
from numpy import cos
from numpy import pi
from numpy import e

import ipywidgets as widgets
from IPython import display as display

import matplotlib.pyplot as plt
import numpy as np


def create_button():
  button = widgets.Button(
    description='Next Iteration',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Next Iteration',
    icon='check' # (FontAwesome names without the `fa-` prefix)
  )
  return button


lower_limit=-5
upper_limit=5

n_particles=10
n_dimensions=2


def f(x,y):
    #Ackley function 2D
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * pi * x)+cos(2 * pi * y))) + e + 20


# Initialize the particle positions and their velocities
X = lower_limit + 0.25*(upper_limit - lower_limit) * np.random.rand(n_particles, n_dimensions) 
assert X.shape == (n_particles, n_dimensions)
V = -(upper_limit - lower_limit)+2*(upper_limit - lower_limit)*np.random.rand(n_particles, n_dimensions)

flagVal = [np.inf,np.inf]

# Initialize the global and local fitness to the worst possible
fitness_gbest, fitness_lbest = [], []
fitness_gbest.append(flagVal)


#fitness_lbest = fitness_gbest * np.ones(n_particles, n_dimensions) 
for it in range (0, n_particles):         
    fitness_lbest.append(flagVal)



X_lbest = 1*X
X_gbest = [1*X_lbest[0][0], 1*X_lbest[0][1]]
fitness_X = np.zeros(X.shape)


for I in range(0, n_particles):
    if f(X_lbest[I][0], X_lbest[I][1])<f(X_gbest[0],X_gbest[1]):
        X_gbest[0]=1*X_lbest[I][0]
        X_gbest[1]=1*X_lbest[I][1]


count=0

def iteration(b):
    global count
    global X,X_lbest,X_gbest,V

# Loop until convergence, in this example a finite number of iterations chosen
    weight=0.5   
    C1=0.2       
    C2=0.3       

    display.clear_output(wait=True)
    display.display(button)
    count+=1

    print (count,"Best particle in:",X_gbest," gbest: ",f(X_gbest[0],X_gbest[1])) #quien gana hasta el momento 

    # Update the particle velocity and position
    for I in range(0, n_particles):
        for J in range(0, n_dimensions):
          R1 = np.random.rand()#uniform_random_number()
          R2 = np.random.rand()#uniform_random_number()
          V[I][J] = (weight*V[I][J]
                    + C1*R1*(X_lbest[I][J] - X[I][J]) 
                    + C2*R2*(X_gbest[J] - X[I][J]))
          X[I][J] = X[I][J] + V[I][J] 
        if f(X[I][0], X[I][1])<f(X_lbest[I][0], X_lbest[I][1]):
            X_lbest[I]=1*X[I]
            if f(X_lbest[I][0], X_lbest[I][1])<f(X_gbest[0], X_gbest[1]):
                X_gbest=1*X_lbest[I] 
          


button=create_button()
button.on_click(iteration)
display.display(button)
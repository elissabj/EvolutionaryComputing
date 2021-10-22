#Rastrigin function 3D
#Example of PSO based on the wikipedia entry
#Elisa Ramos Gomez
#Last modification: 19 oct 2021 16:55 

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


lower_limit=-4
upper_limit=4

n_particles=100
n_dimensions=3


def f(x,y,z):
    #Rastrigin function 3D
    A = 10
    fit = A*3 
    
    fit += (x**2 - A* cos(2*pi*x)) + (y**2 - A* cos(2*pi*y))+(z**2 - A* cos(2*pi*z))
    return fit


# Initialize the particle positions and their velocities
X = lower_limit + 0.25*(upper_limit - lower_limit) * np.random.rand(n_particles, n_dimensions) 
assert X.shape == (n_particles, n_dimensions)

V = -(upper_limit - lower_limit)+3*(upper_limit - lower_limit)*np.random.rand(n_particles, n_dimensions)

flagVal = [np.inf,np.inf, np.inf]

# Initialize the global and local fitness to the worst possible
fitness_gbest, fitness_lbest = [], []
fitness_gbest.append(flagVal)


#fitness_lbest = fitness_gbest * np.ones(n_particles, n_dimensions) 
for it in range (0, n_particles):        
    fitness_lbest.append(flagVal)



X_lbest = 1*X
X_gbest = [1*X_lbest[0][0], 1*X_lbest[0][1], 1*X_lbest[0][2]]



fitness_X = np.zeros(X.shape)


for I in range(0, n_particles):
    if f(X_lbest[I][0], X_lbest[I][1], X_lbest[I][2])<f(X_gbest[0],X_gbest[1],X_gbest[2]):
        X_gbest[0]=1*X_lbest[I][0]
        X_gbest[1]=1*X_lbest[I][1]
        X_gbest[2]=1*X_lbest[I][2]




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

    print (count,"Best particle in:",X_gbest," gbest: ",f(X_gbest[0],X_gbest[1],X_gbest[2])) #quien gana hasta el momento 

    # Update the particle velocity and position
    for I in range(0, n_particles):
        for J in range(0, n_dimensions):
          R1 = np.random.rand()#uniform_random_number()
          R2 = np.random.rand()#uniform_random_number()
          V[I][J] = (weight*V[I][J]
                    + C1*R1*(X_lbest[I][J] - X[I][J]) 
                    + C2*R2*(X_gbest[J] - X[I][J]))
          X[I][J] = X[I][J] + V[I][J] 
        if f(X[I][0], X[I][1], X[I][2])<f(X_lbest[I][0], X_lbest[I][1], X_lbest[I][2]):
            X_lbest[I]=1*X[I]
            if f(X_lbest[I][0], X_lbest[I][1], X_lbest[I][2])<f(X_gbest[0], X_gbest[1],X_gbest[2]):
                X_gbest=1*X_lbest[I] 
          


button=create_button()
button.on_click(iteration)
display.display(button)

# EvolutionaryComputing

Repository with some of the evolutionary algorithms to solve problems, highly recommend used Google Collab.
If you wan't to know more of this topics (Spanish language), please check this link: 
https://drive.google.com/file/d/1H2VfEJNmvxyQP3iDVBxPZsBzEpiWL7zR/view?usp=sharing



   ## Practice 1: Dynamic Programming 
   DP is a paradigm that solves problems by combining subproblems once then saving the result.
   This subproblems overlapping and the principal characteristics are:
    - Using to optimizing problems.
    - They can have many solutions. 
    - Each solution we can found, one solution with a local optimal value (maximum, minimum).
    - We can reconstruct which values are part of the solution.

      Problems to solve:
      - Snapsack problem.
      - Coin Change.
      - Stairs.
    
    
    
   ## Practice 2: Dynamic Programming 2  
      Problems to solve:
      - Matrix Chain Multiplication.



   ## Practice 3: Genetic Algorithm 
   It refers to a series of steps to solve a problem then when combining it with genetics, simulate
   the evolution of species to formulate the steps to follow with the same objective to solve problems.
   
      Problems to solve:
      - Genetic Algorithm (GAS) to minimize Ackley's function in 2D.
      - GAS to minimize Rastrigin's function in 3D.
   
   
   
   ## Practice 4: Combinatorial Optimization 
   Combinatorial optimizations are problems where the solution space is made up of subsets, subarrays,
   but finding a solution set is very complicated even for moderate-sized problems, so genetic algorithms 
   help us to find a valid solution or a good approximation.
   
      Problems to solve:
      - GAS to Knapsack problems with a total weight (0,1) and 20 items random integer values in the interval [1,100].
      - GAS to TSP problem for 7 cities.



   ## Practice 5: Fractals
   A Fractal is a type of mathematical shape that are infinitely complex. In essence, a Fractal is a pattern 
   that repeats forever, and every part of the Fractal, regardless of how zoomed in, or zoomed out you are, 
   it looks very similar to the whole image.
   
      Problems to solve:
      - Draw a landspace with fractals. reference: http://www.fgalindosoria.com/ecuaciondelanaturaleza/


   
   ## Practice 6: Particle Swarm Optimization
   This idea starts from the observation of what a swarm is (a large group of individuals such as animals, 
   people, etc.) that has movement, that is, they move together. 
  
      Problems to solve:
      - PSO to minimize Ackley's function in 2D.
      - PSO to minimize Rastrigin's function in 3D.



   ## Practice 7: Particle Systems
   Once again Alan Turing makes a biological proposal called morphogens, of the last publications before 
   dying where the cells of an organism in an early stage of its development are visualized as a collection 
   of "cells" that have communication and influence from the closest neighbors. 
   
      Problems to solve:
      - PS in 2D with nearest neighbor interactions in a grid.
      - PS in 2D with collisions.
   

   ## Practice 8: SOM
   Self-organizing maps are a type of neural network with competitive learning since influence and intertia
   are combined to avoid minimizing error, resulting in a better understanding of the problem.
   
      Problems to solve:
         - SOM using at least 10 indicators about at least 40 countries from the database in the World Bank
         
   ## Practice 9: Cellular Automaton 
   The Game of Life
   
         Problems to solve:
         - S = infinite rectangular grid.
           N = {closest neighbors} U {self}
           Q = {0,1,2}
           δ = (b1, b2, s1, s2, u1, u2, r1, r2)
           
         - S = Infinite 1-D grid.
           N = {First 2 layers of closest neighbors} U {self} (| N | = 5)
           Q = {0,1}
           δ = W110 and δ = W110R

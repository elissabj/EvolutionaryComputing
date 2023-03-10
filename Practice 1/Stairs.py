
import sys
 
#Define the limit of the recusion
sys.setrecursionlimit(9000000)

memory = [-1]*20000

def stairs (nStairs: int, kJumps: int):

    if nStairs == 0:
        return 1
    
    if nStairs < 0:
        return 0
    
    if memory[nStairs] != -1:
        return memory[nStairs]

    sumJumps = 0

    for i in range(1, kJumps+1):
        sumJumps = sumJumps + stairs(nStairs-i, kJumps)

    memory[nStairs] = sumJumps
    return sumJumps



nStairs, kJumps = input().split()
nStairs = int(nStairs)
kJumps = int(kJumps)

print(stairs(nStairs, kJumps))
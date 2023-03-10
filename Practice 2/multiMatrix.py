def matrixDP():
    memory = []
    for i in range (0,1000):
        rows = []
        for i in range(0,1000):
            rows.append(-1)
        memory.append(rows)
    
    return memory

def multiMatrix (v, i, j):

    if i == j:
        return 0
    
    if memory[i][j] != -1:
        return memory[i][j]

    memory[i][j] = 1e6

    for k in range (i, j):
        memory[i][j] = min(memory[i][j], (multiMatrix(v,i,k) + multiMatrix(v,k+1, j) + v[i-1] * v[k] * v[j]) )

    return memory[i][j]


memory = matrixDP()
lenght = int(input())
values = input().split()

for i in range (0, len(values)):
    values[i] = int(values[i])

print (multiMatrix(values,1, lenght-1))
import numpy as np

with open('input.txt','r') as data:
    readings = [line.strip('\n') for line in data.readlines()]
    readings = [[int(x) for x in y.split()] for y in readings]
    

total = 0

for reading in readings:
    pyramid = [reading]
    
    while sum(pyramid[-1]) != 0:
        next_row = list(np.diff(pyramid[-1]))
        pyramid.append(next_row)
        
    for n in range(len(pyramid)-1,-1,-1):
        if n == len(pyramid)-1:
            pyramid[n].append(0)
        else:
            pyramid[n].append(pyramid[n][-1] + pyramid[n+1][-1])
            
    total += pyramid[0][-1]
    
print(total)
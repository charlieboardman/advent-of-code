N1 = []
N2 = [] #Init lists N for both of the lists of numbers n

with open('input', 'r') as input_file:
    for line in input_file:
        n1, n2 = line.split()
        #print(f'{n1} {n2}')
        N1.append(int(n1))
        N2.append(int(n2))
        
N1.sort()
N2.sort()

total = 0
for i in range(len(N1)):
    diff = abs(N1[i] - N2[i])
    total += diff
    
print(total)
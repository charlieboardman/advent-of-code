N1 = []
N2 = []
with open('input', 'r') as input_file:
    for line in input_file:
        n1, n2 = line.split()
        #print(f'{n1} {n2}')
        N1.append(int(n1))
        N2.append(int(n2))

N1_total = 0
for n in N1:
    N1_total += n * N2.count(n)
    
print(N1_total)
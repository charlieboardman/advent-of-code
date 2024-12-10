disk_compact = [int(c) for c in open('input').read().strip('\n')]
disk_expounded = [['f',c,int(i/2)] if i%2 == 0 else ['s',c] for i,c in enumerate(disk_compact)]
#remove zero space
disk_expounded = [x for x in disk_expounded if x != ['s',0]]
disk_expounded_og = [x for x in disk_expounded]
print(disk_expounded)

i = len(disk_expounded) - 1
while i >= 0:
    
    print(i)
    
    if disk_expounded[i][0] == 'f':
        j = next((j for j,c in enumerate(disk_expounded) if c[0] == 's' and c[1] >= disk_expounded[i][1]),None)
        if j == None or j > i: #No space found
            i -= 1
            continue
        else:
            disk_expounded.insert(j,disk_expounded[i])
            disk_expounded[j+1][1] -= disk_expounded[i+1][1]
            disk_expounded[i+1] = ['s',disk_expounded[i+1][1]]
            if disk_expounded[j+1][1] == 0:
                disk_expounded.pop(j+1)
                i -= 1
                continue
            continue
    else:
        i -= 1
        continue
    
print(disk_expounded)

#Build out disk string from part a
disk = []
for x in disk_expounded:
    if x[0] == 'f':
        disk += [str(x[2]) for _ in range(x[1])]
    elif x[0] == 's':
        disk += ['.' for _ in range(x[1])]
mine = ''.join(disk)
print(f'Mine: {mine}')
correct = '00992111777.44.333....5555.6666.....8888..'
print(f'Corr: {correct}')

print(f'Successful: {correct == mine}')

checksum = sum([i*int(n) if n.isnumeric() else 0 for i,n in enumerate(list(mine))])

print(f'Checksum: {checksum}')


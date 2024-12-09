disk_compact = [int(c) for c in open('input').read().strip('\n')]

disk = []
i = 0
while i < len(disk_compact):
    if i%2 == 0:
        data = 'file'
    elif i%2 == 1:
        data = 'space'
        
    data_id = int(i/2)
    
    if data == 'file':
        disk += [str(data_id) for x in range(disk_compact[i])]
    elif data == 'space':
        disk += ['.' for x in range(disk_compact[i])]
    
    i += 1

print(''.join(disk))
 
def move_rightmost_digit(disk): #Returns disk and whether sorting is complete
    #Find rightmost digit
    i_back = len(disk) - 1
    while not disk[i_back].isnumeric():
        i_back -= 1
        
    #Find leftmost open spot
    i = 0
    while disk[i].isnumeric():
        i += 1
    
    if i > i_back: #If the leftmost open spot is right of the rightmost digit, we're done
        return disk, True
        
    #Take rightmost digit, move it to the leftmost open spot
    disk[i] = disk[i_back]
    
    #Fill old digit spot with period
    disk[i_back] = '.'
    
    return disk, False

#Find iterations to know how much progress we've made
#Find rightmost digit
i_back = len(disk) - 1
while not disk[i_back].isnumeric():
    i_back -= 1
total_iterations = len([x for i,x in enumerate(disk) if not x.isnumeric() and i < i_back]) - 1
iterations = 1

og_disk = [x for x in disk]

complete = False
while complete == False:
    disk, complete = move_rightmost_digit(disk)
    print(f'{iterations}/{total_iterations}')
    iterations += 1
    
print(''.join(disk))

integrity_check_numbers = sorted([x for x in disk if x.isnumeric()]) == sorted([x for x in og_disk if x.isnumeric()])
integrity_check_dots = og_disk.count('.') == disk.count('.')
print(f'Check integrity numbers: {integrity_check_numbers}')
print(f'Check integrity dots: {integrity_check_dots}') 

checksum = sum([i*int(n) for i,n in enumerate(disk) if n.isnumeric()])

print(checksum)
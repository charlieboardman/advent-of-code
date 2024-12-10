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
 
def find_rightmost_file(disk,file_end): #Returns slicing index for rightmost file
    #Find rightmost file. In first call, file_end = len(disk)
    while disk[file_end-1] == '.':
        file_end -= 1
        
    #Scan rightmost file
    file_start = file_end - 1
    while disk[file_start-1] == disk[file_end-1]: #While in the same data id
        file_start -= 1
        if file_start == 0:
            return file_start, file_end
    
    return file_start, file_end

def find_leftmost_fitting_space(disk,size_needed,space_start,file_start): #Returns slicing index for leftmost big enough space
    pointer = space_start
    if pointer > file_start:
        return 0,0,False
    while pointer < file_start:
        while disk[pointer] != '.':
            pointer += 1 #Find the first space
            if pointer > file_start:
                return 0,0,False
            
        #First space found, now extend out to see how long it is
        anchor = pointer
        while disk[pointer] == '.':
            pointer += 1
            if pointer - anchor >= size_needed:
                return anchor,pointer,True
    
    return 0,0,False
                
complete = False
file_end = len(disk)
space_start = 0
disk_str = ''.join(disk)
while not complete:
    print(file_end)
    #print(disk_str)
    file_start,file_end = find_rightmost_file(disk,file_end)
    space_start,space_end,space_found = find_leftmost_fitting_space(disk,(file_end-file_start),0,file_start)
    
    if file_start == 0:
        break
     
    #Reassign
    if space_found:
        disk[space_start:space_end] = disk[file_start:file_end]
        disk[file_start:file_end] = ['.'] * (file_end - file_start)
        disk_str = ''.join(disk)
    else:
        file_end = file_start

mine = ''.join(disk)
#corr = '00992111777.44.333....5555.6666.....8888..'

print(f'Mine: {mine}')
#print(f'Corr: {corr}')
#print(f'Correct: {mine==corr}')

checksum = sum([i*int(n) for i,n in enumerate(disk) if n.isnumeric()])

print(checksum)
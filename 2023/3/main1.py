with open('input.txt','r') as input_file:
    schematic = input_file.readlines()

def expand_indices_by_1(row,n,length_num,length_line): #Finds the indices to look one adjacent horizontally from a number
    #Takes the index n of the space immediately following a number, and the length of that number
    i = n - length_num - 1
    if i == -1:
        i = 0 #Fix the case where the number is leftmost
    
    j = n + 1
    
    
    return i,j

def adj_symbol(row,i,j,length_num):
    
    #Handle corner cases of first and last row
    if row == 0:
        adjacent_row_slice = schematic[1][i:j]
        if any([x for x in adjacent_row_slice if x != '.' and not x.isnumeric()]):
            return True
        if schematic[row][i] != '.' or schematic[row][j] != '.':
            return True
        else:
            return False
    #Last row
    if row == len(schematic) - 1:
        adjacent_row_slice = schematic[row-1][i:j]
        if any([x for x in adjacent_row_slice if x != '.' and not x.isnumeric()]):
            return True
        if schematic[row][i] != '.' or schematic[row][j] != '.':
            return True
        else:
            return False
        
    #All middle rows
    adjacent_row_slice_up = schematic[row-1][i:j]
    adjacent_row_slice_down = schematic[row+1][i:j]
    adjacent_left = schematic[row][i]
    
    if n == len(line)-1:
        adjacent_right = schematic[row][j-1]
    else:
        adjacent_right = schematic[row][j]
    
    if any([x for x in adjacent_row_slice_up if x != '.' and not x.isnumeric()]):
        return True
    if any([x for x in adjacent_row_slice_down if x != '.' and not x.isnumeric()]):
        return True
    if adjacent_left != '.' and not adjacent_left.isnumeric():
        return True
    if adjacent_right != '.' and not adjacent_right.isnumeric():
        return True
    
    return False


total = 0

for row,line in enumerate(schematic):

    if row == 23:
        pass

    line = line.strip('\n')
    running_num = ''
    
    for n in range(len(line)):
        
        if running_num == '540':
            pass
        
        if line[n].isnumeric():
            running_num += line[n]
            
        if running_num and not line[n].isnumeric(): #Just ended a number
            i,j = expand_indices_by_1(row,n,len(running_num),len(line))
            is_adjacent = adj_symbol(row,i,j,len(running_num))
            if is_adjacent:
                total += int(running_num)
            
        if not line[n].isnumeric():
            running_num = ''
        
        if n == len(line) - 1 and running_num:
            i,j = expand_indices_by_1(row,n,len(running_num),len(line))
            i = i+1 #Fix for corner case where cursor is rightmost
            is_adjacent = adj_symbol(row,i,j,len(running_num))
            if is_adjacent:
                total += int(running_num)
        
        continue

print(total)
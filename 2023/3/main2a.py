with open('input.txt','r') as input_file:
    schematic = input_file.readlines()

LINE_LENGTH = len(schematic[0].strip('\n')) - 1
SCHEM_HEIGHT = len(schematic) - 1

def find_surrounding(row,start,end):
    chars_around = ''
    if start == 0 and row == 0: #top left
        chars_around += schematic[row][end]
        chars_around += schematic[row+1][0:end+1]
        return chars_around
    
    if end == LINE_LENGTH and row == 0: #top right
        chars_around += schematic[row][start-1]
        chars_around += schematic[row+1][start-1:end]
        return chars_around
        
    if start == 0 and row == SCHEM_HEIGHT: #bottom left
        chars_around += schematic[row-1][start:end+1]
        chars_around += schematic[row][end]
        return chars_around
    
    if end == LINE_LENGTH and row == SCHEM_HEIGHT: #bottom right
        chars_around += schematic[row-1][start-1:end]
        chars_around += schematic[row][start-1]
        return chars_around
    
    if row == 0: #top
        chars_around += schematic[row][start-1]
        chars_around += schematic[row][end]
        chars_around += schematic[row+1][start-1:end+1]
        return chars_around
        
    if row == SCHEM_HEIGHT: #bottom
        chars_around += schematic[row][start-1]
        chars_around += schematic[row][end]
        chars_around += schematic[row-1][start-1:end+1]
        return chars_around
    
    if end == LINE_LENGTH: #rightmost
        chars_around += schematic[row-1][start-1:end]
        chars_around += schematic[row][start-1]
        chars_around += schematic[row+1][start-1:end]
        return chars_around
        
    if start == 0: #leftmost
        chars_around += schematic[row-1][start:end+1]
        chars_around += schematic[row][end]
        chars_around += schematic[row+1][start:end+1]
        return chars_around
        
    #Normal case
    chars_around += schematic[row-1][start-1:end+1]
    chars_around += schematic[row][start-1]
    chars_around += schematic[row][end]
    chars_around += schematic[row+1][start-1:end+1]
    return chars_around
        
total = 0
pns = []

for row,line in enumerate(schematic):
    print(f'Running row {row}/139 part 1')
    #print(row,' part 1')
    if row == 4:
        pass

    start = end = None

    line = line.strip('\n')
    
    for n in range(LINE_LENGTH+1):
        
        #print(line[n])
        
        if line[n].isnumeric() and start == None:
            start = n
        
        if n == LINE_LENGTH and start != None:
            end = n
        
        if not line[n].isnumeric() and start != None:
            end = n
            
        if start != None and end != None:
            chars_around = find_surrounding(row,start,end)
            if end == LINE_LENGTH and line[end].isnumeric():
                number = int(line[start:end+1])
            else:
                number = int(line[start:end])
            
            if any([x for x in chars_around if x != '.' and not x.isnumeric()]):
                total += number
                pns.append((row,start,end))                
                
            number = 0
            start = end = None

print(total)

#Part 2 starts here
def find_start(row,n):
    while schematic[row][n-1].isnumeric():
        n -= 1
    return n

def find_end(row,n):
    while schematic[row][n+1].isnumeric():
        n += 1
    return n+1

def find_adj_nums(schematic,row,n): #Expands around a point on the schematic until all adjacent numbers are encompassed
    adj_nums = []
    #Above
    row_cursor = row-1
    n_cursor = n+1
    while n_cursor >= n-1:
        if schematic[row_cursor][n_cursor].isnumeric():
            number = [] #Has the format [row,start,end]
            number.append(row_cursor)
            number.append(find_start(row_cursor,n_cursor)) #Starting location
            number.append(find_end(row_cursor,n_cursor))
            n_cursor = number[1] #Set the cursor
            adj_nums.append(number)
        n_cursor -= 1 #Move the cursor left
            
    #Right
    if schematic[row][n+1].isnumeric():
        number = []
        number.append(row)
        number.append(n+1)
        number.append(find_end(row,n+1))
        adj_nums.append(number)
    
    #Left
    if schematic[row][n-1].isnumeric():
        number = []
        number.append(row)
        number.append(find_start(row,n-1))
        number.append(n)
        adj_nums.append(number)
    
    #Below
    row_cursor = row+1
    n_cursor = n+1
    while n_cursor >= n-1:
        if schematic[row_cursor][n_cursor].isnumeric():
            number = [] #Has the format [row,start,end]
            number.append(row_cursor)
            number.append(find_start(row_cursor,n_cursor)) #Starting location
            number.append(find_end(row_cursor,n_cursor))
            n_cursor = number[1] #Set the cursor
            adj_nums.append(number)
        n_cursor -= 1 #Move the cursor left
    
    adj_nums_values = [schematic[x[0]][x[1]:x[2]] for x in adj_nums]
    
    return adj_nums_values


gear_ratio_sum = 0

for row in range(SCHEM_HEIGHT+1):
    print(f'Running row {row}/139 part 2')
    for n in range(LINE_LENGTH+1):
        char = schematic[row][n]
        if char != '.' and not char.isnumeric():
            adj_nums = find_adj_nums(schematic,row,n)
            
            if len(adj_nums) == 2:
                gear_ratio = int(adj_nums[0]) * int(adj_nums[1])
                gear_ratio_sum += gear_ratio
            

print(gear_ratio_sum)

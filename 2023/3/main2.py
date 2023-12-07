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

adj_nums = []

gear_ratio_sum = 0

for row,line in enumerate(schematic):
    #print(row,' part 2')
    line = line.strip('\n')
    for n in range(LINE_LENGTH+1):
        
        if row == 1 and n == 62:
            pass
        
        #ch = line[n]
        #print(ch)
        
        if line[n] != '.' and not line[n].isnumeric():
            adj_nums = []
            #above
            cursor_row = row-1
            cursor_n = n+1
            while cursor_n >= n-1:
                if schematic[cursor_row][cursor_n].isnumeric():
                    start = find_start(cursor_row,cursor_n)
                    end = find_end(cursor_row,cursor_n)
                    adj_nums.append((cursor_row,start,end))
                    cursor_n = start
                    #print(schematic[cursor_row][start:end])
                cursor_n -= 1
            
            #right
            if line[n+1].isnumeric():
                end = find_end(row,n+1)
                adj_nums.append((row,n+1,end))
                #print(schematic[row][n+1:end])
            
            #left
            if line[n-1].isnumeric():
                start = find_start(row,n-1)
                adj_nums.append((row,n-1,end))
                #print(schematic[row][n-1:end])
            
            #below
            if row == SCHEM_HEIGHT:
                continue
            cursor_row = row+1
            cursor_n = n+1
            while cursor_n >= n-1:
                if schematic[cursor_row][cursor_n].isnumeric():
                    start = find_start(cursor_row,cursor_n)
                    end = find_end(cursor_row,cursor_n)
                    adj_nums.append((cursor_row,start,end))
                    cursor_n = start
                    #print(schematic[cursor_row][start:end])
                cursor_n -= 1
                
            if len(adj_nums) == 2:
                gear_ratio = 1
                for pn in adj_nums:
                    row = pn[0]
                    start = pn[1]
                    end = pn[2]
                    
                    gear_ratio *= int(schematic[row][start:end])
                    
                gear_ratio_sum += gear_ratio
                adj_nums = []
                

print(gear_ratio_sum)
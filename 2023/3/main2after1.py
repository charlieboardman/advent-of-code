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
        
        if row == 1 and n == 63:
            pass
        
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
                    print(schematic[cursor_row][start:end])
                cursor_n -= 1
            
            #right
            if line[n+1].isnumeric():
                end = find_end(row,n+1)
                adj_nums.append((row,n+1,end))
                print(schematic[row][n+1:end])
            
            #left
            if line[n-1].isnumeric():
                start = find_start(row,n-1)
                adj_nums.append((row,n-1,end))
                print(schematic[row][n-1:end])
            
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
                    print(schematic[cursor_row][start:end])
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
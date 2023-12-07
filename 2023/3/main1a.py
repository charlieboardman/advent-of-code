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

for row,line in enumerate(schematic):

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
                
            number = 0
            start = end = None
            
print(total)
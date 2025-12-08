with open('input.txt') as f:
    rows = f.read().splitlines()
    rows = [list(row) for row in rows]

global_array = rows.copy()

max_x = len(global_array[0]) - 1
max_y = len(global_array) - 1

def is_roll(x,y):
    if global_array[y][x] == '@':
        return True
    else:
        return False

def count_adjacents(x,y):
    count = 0
    #Check all 8 directions, starting at right, moving counterclockwise
    #pos 0
    if x < max_x:
        count += is_roll(x+1,y)
    #pos 1
    if x < max_x and y > 0:
        count += is_roll(x+1,y-1)
    #pos 2
    if y > 0:
        count += is_roll(x,y-1)
    #pos 3
    if x > 0 and y > 0:
        count += is_roll(x-1,y-1)
    #pos 4
    if x > 0:
        count += is_roll(x-1,y)
    #pos 5
    if x > 0 and y < max_y:
        count += is_roll(x-1,y+1)
    #pos 6
    if y < max_y:
        count += is_roll(x,y+1)
    #pos 7
    if x < max_x and y < max_y:
        count += is_roll(x+1,y+1)
        
    return count

total = 0

removables = 1 #init to a non-zero

while removables:
    removed = 0
    removables = 0
    working_array = global_array.copy()
    
    for x in range(max_x+1):
        for y in range(max_y+1):
            removable = is_roll(x,y) and count_adjacents(x,y) < 4
            removables += removable
            total += removable
            if removable:
                working_array[y][x] = '.'
    
    global_array = working_array.copy()
        
print(total)

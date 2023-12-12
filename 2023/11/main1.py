with open('input.txt','r') as input_file:
    galaxy_map_lines = [line.strip('\n') for line in input_file.readlines()]
    
    galaxy_map = [[x for x in y] for y in galaxy_map_lines]

row = 0
col = 0

#Sweep rows
while row < len(galaxy_map):
    if not '#' in galaxy_map[row]:
        galaxy_map.insert(row,['.' for char in galaxy_map[row]])
        row += 1
    row += 1

#Sweep columns
while col < len(galaxy_map[0]):
    constructed_column = []
    for row in range(len(galaxy_map)):
        constructed_column.append(galaxy_map[row][col])
    
    if not '#' in constructed_column:
        for row in range(len(galaxy_map)):
            galaxy_map[row].insert(col,'.')
        col += 1
    
    col += 1
    
#galaxy_map is now expanded
    
#number the galaxies
gal_num = 1
for row in range(len(galaxy_map)):
    for col in range(len(galaxy_map[row])):
        if galaxy_map[row][col] == '#':
            galaxy_map[row][col] = gal_num
            gal_num += 1
        else:
            galaxy_map[row][col] = 0
            
num_galaxies = gal_num - 1

num_connections = (num_galaxies)*(num_galaxies - 1)//2

print(f'# gal: {num_galaxies}')
print(f'# con: {num_connections}')


def calc_distance(gal1,gal2):

    row_gal_1 = [[gal1 in row] for row in galaxy_map].index([True])
    row_gal_2 = [[gal2 in row] for row in galaxy_map].index([True])
    
    col_gal_1 = [[col == gal1] for col in galaxy_map[row_gal_1]].index([True])
    col_gal_2 = [[col == gal2] for col in galaxy_map[row_gal_2]].index([True])
        
    distance = abs(row_gal_1 - row_gal_2) + abs(col_gal_1 - col_gal_2)
    return distance

distances = []
gal_check = 1
gal_cursor = num_galaxies

while gal_check < num_galaxies:
    while gal_cursor > gal_check:
        distances.append(calc_distance(gal_check,gal_cursor))
        gal_cursor -= 1
    gal_check += 1
    gal_cursor = num_galaxies

        
    #print(f'{gal_check}/{num_galaxies}')

print(sum(distances))
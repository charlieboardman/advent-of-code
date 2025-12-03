with open('input.txt') as input_file:
    commands = [line.strip() for line in input_file.readlines()]
    
arrow = 50
count = 0

for command in commands:
    direction = command[0]
    distance = int(command[1:])
    
    if direction == 'R':
        arrow = (arrow + distance) % 100 #use 100 because 100%100 = (99+1)%100 = 0
        
    elif direction == 'L':
        arrow = (arrow - distance) % 100
        
    if arrow == 0:
        count += 1
        
#Merry Christmas! Christ is born!
        
print(count)
with open('input.txt') as input_file:
    commands = [line.strip() for line in input_file.readlines()]
    
arrow = 50
total_passes = 0

for command in commands:
    direction = command[0]
    distance = int(command[1:])
    
    if direction == 'R':
        passes = (arrow + distance)//100
        arrow = (arrow + distance)%100
        
    elif direction == 'L':
        #Direction doesn't matter, and the int floor works if turning right, so calcuate the passes by 0 by just flipping the position and rotation
        #You still have to %100 it in case arrow is at 0
        flipped_arrow = (100-arrow)%100 
        passes = (flipped_arrow + distance)//100
        arrow = (arrow - distance)%100 #But you still have to calcuate new arrow position in the leftward direction
        
    total_passes += passes
        
#Merry Christmas! Christ is born! Welcome to AOC2025!!
        
print(total_passes)

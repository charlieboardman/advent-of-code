with open('input.txt','r') as input_file:
    lines = [line.strip('\n') for line in input_file.readlines()]
    
    sequence = lines[0]
    
    instructions_raw = lines[2::]
    
keys = [x[0:3] for x in instructions_raw]
values = [[x[7:10],x[12:15]] for x in instructions_raw]

inst = dict(zip(keys,values))
LRkey = {'L':0,'R':1}

steps = 0
len_seq = len(sequence)

location = 'AAA'

while location != 'ZZZ':
    direc = sequence[steps%len_seq]
    location = inst[location][LRkey[direc]]
    steps += 1
    
print(steps)
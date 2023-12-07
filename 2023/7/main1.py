with open('input.txt','r') as input_file:
    lines = input_file.readlines()

lines = [line.strip('\n') for line in lines]

hands = [[x.split()[0],int(x.split()[1])] for x in lines]

hands_broken_down = []

for hand in hands:
    breakdown = [[x,hand[0].count(x)] for x in hand[0]]
    breakdown = [x+str(y) for x,y in breakdown]
    breakdown = list(set(breakdown))
    breakdown = [[x[0],int(x[1])] for x in breakdown]
    
    hand.append(breakdown)
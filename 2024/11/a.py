with open('input') as f:
    stones = f.read().strip('\n').split(' ')
    
def blink(stones):
    i = 0
    length = len(stones)
    while i < length: #length may change as we split stones, so need it to be variable
        num = stones[i]
        if num == '0':
            stones[i] = '1'
            i += 1
            continue
        if (num_len := len(num))%2 == 0:
            left = num[0:int(num_len/2)]
            right = num[int(num_len/2):]
            stones.insert(i,left)
            stones[i+1] = str(int(right)) #Eliminate leading zeros
            length += 1 #We added a stone
            i += 2 #Go forward 2 because we inserted a new number into the list
            continue
        else:
            stones[i] = str(2024*int(num))
            i += 1
            continue
    return stones
        

for i in range(25):
    stones = blink(stones)
    print(f'Run {i+1} times')
    
print(len(stones))
from functools import cache
from collections import Counter

with open('input') as f:
    stones = f.read().strip('\n').split(' ')

@cache
def process_num(num):
    if num == '0':
        return ['1']
    elif len(num)%2 == 0:
        left = num[0:int(len(num)/2)]
        right = num[int(len(num)/2):]
        return [left,str(int(right))]
    else:
        return [str(2024*int(num))]
        
stones = Counter(stones)
blinks = 0

#print('Initial:')
#print(stones)

while blinks < 75:
    #Process through each existing number based on the keys to the dict
    keys = list(stones.keys())
    working_copy_stones = Counter()
    for key in keys:
        quantity = stones[key]
        new_nums = process_num(key)
        del stones[key] #We are processing all of them so this goes to zero
        for new_num in new_nums:
            working_copy_stones[new_num] += quantity
    
    stones = working_copy_stones
    blinks += 1
    #print(f'{blinks} times:')
    #print(stones)

print(sum(stones.values()))
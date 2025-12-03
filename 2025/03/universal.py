with open('input.txt') as f:
    banks = [[n for n in line] for line in f.read().splitlines()]

def max_joltage(bank,digits):
    #Starting from the left, look at each number bank[i]. If bank[i+1] > bank[i], del bank[i]
    bank = bank.copy() #Don't mess with the original spot in memory, no side effects
    while len(bank) > digits:
        for i in range(1,len(bank)):
            if bank[i]>bank[i-1]: 
                del bank[i-1]
                break
        else:
            del bank[i] #If we reached the end without breaking, just remove that one
    
    ints = [int(c)*(10**((digits-1)-x)) for c,x in zip(bank,range(digits))]
    return sum(ints)

p2 = p1 = 0

for bank in banks:
    p1 += max_joltage(bank,2)
    p2 += max_joltage(bank,12)

print(f'p1: {p1}')
print(f'p2: {p2}')
        

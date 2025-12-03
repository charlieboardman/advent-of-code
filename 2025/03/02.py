with open('input.txt') as f:
    banks = [[n for n in line] for line in f.read().splitlines()]

def max_joltage_p2(og_bank,bank): #Let's try pulling out small digits until we get 12 left
    #Starting from the left, look at each number bank[i]. If bank[i+1] > bank[i], del bank[i]
    while len(bank) > 12:
        for i in range(1,len(bank)):
            if bank[i]>bank[i-1]: 
                del bank[i-1]
                break
        else:
            del bank[i] #If we reached the end without breaking, just remove that one
    
    ints = [int(c)*(10**(11-x)) for c,x in zip(bank,range(12))]
    return sum(ints),og_bank


p2 = 0

for bank in banks:
    su,og_bank = max_joltage_p2(bank.copy(),bank)
    print(su)
    print(og_bank)
    p2 = p2 + su

print(f'p2: {p2}')
        
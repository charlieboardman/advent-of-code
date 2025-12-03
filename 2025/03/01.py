with open('input.txt') as f:
    banks = f.read().splitlines()

def max_joltage(bank):
#Find the digit for the tens place
    tens_i = bank.find(max(bank)) #Find the first instance of the largest digit in the bank
    if tens_i == len(bank)-1: #If the largest digit only comes at the end, find the next largest
        tens_i = bank.find(max(bank[:-1]))
        
    #Use the largest usable digit for the tens place
    tens = bank[tens_i]
    
    #Get the max digit after the one used in the tens place
    remainder = bank[tens_i+1:]

    ones_i = remainder.find(max(remainder)) + (tens_i+1) #Add back the index of the tens digit since we sliced the bank
    ones = bank[ones_i]
    
    return 10*int(tens)+int(ones)
    
p1 = sum([max_joltage(bank) for bank in banks])
print(f'p1: {p1}')
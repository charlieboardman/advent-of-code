import re
import math

with open('input') as f:
    mainstr = f.read()

regex_do = r'^do\(\)'
regex_dont = r'^don\'t\(\)'
regex_mul = r'^mul\((\d{1,3},\d{1,3})\)'

counting = True

total = 0

i = 0
while i < min(i+12,len(mainstr)):
    scanstr = mainstr[i:i+12]
    
    if re.search(regex_do,scanstr):
        counting = True
        
    if re.search(regex_dont,scanstr):
        counting = False
    
    mul_search = re.search(regex_mul,scanstr)
    if mul_search and counting:
        total += math.prod([int(x) for x in mul_search.group(1).split(',')])
    
    i += 1
    
print(total)
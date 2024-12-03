import re
with open('input') as f:
    mainstr = f.read()
regex = r'mul\((\d{1,3},\d{1,3})\)'
matches = re.findall(regex,mainstr)
print(sum([int(x[0])*int(x[1]) for x in [y.split(',') for y in matches]]))
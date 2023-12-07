with open('input.txt','r') as p:
    lines = p.readlines()
    total = 0
    for line in lines:
        digits = []
        for c in line:
            if c.isnumeric():
                digits.append(c)
        combined = digits[0] + digits[-1]
        total = total + int(combined)

print(total)
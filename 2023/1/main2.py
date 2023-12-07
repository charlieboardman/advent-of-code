with open('input.txt','r') as p:
    
    digits_txt = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    lines = p.readlines()
    total = 0
    for line in lines:
        digits = []
        running_alpha = ''
        for c in line:
            #If numeric, just continue
            if c.isnumeric():
                digits.append(c)
                running_alpha = ''
            #If alpha, check if the string of alphas ends with a text digit
            if c.isalpha():
                running_alpha += c
                for n in digits_txt.keys():
                    if running_alpha.endswith(n):
                        digits.append(digits_txt[n])
                    
            
        combined = digits[0] + digits[-1]
        total = total + int(combined)

print(total)  
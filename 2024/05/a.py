rules = [(int(line.split('|')[0]),int(line.split('|')[1])) for line in open('testinput') if '|' in line]
updates = [[int(x) for x in line.split(',')] for line in open('testinput') if ',' in line]

correct_updates = [x for x in updates] #We will remove the bad ones from this list. List construction so as not to share memory address
for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                continue
            else:
                correct_updates.remove(update)
                break
                
print(sum([update[int(len(update)/2)] for update in correct_updates]))
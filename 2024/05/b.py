rules = [(int(line.split('|')[0]),int(line.split('|')[1])) for line in open('input') if '|' in line]
updates = [[int(x) for x in line.split(',')] for line in open('input') if ',' in line]

incorrect_updates = []
for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                continue
            else:
                incorrect_updates.append(update)
                break

def swap(swap_list,val1,val2):
    i1 = swap_list.index(val1)
    i2 = swap_list.index(val2)
    swap_list[i1],swap_list[i2] = swap_list[i2],swap_list[i1]

def rectify(update,rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                continue
            else:
                swap(update,rule[0],rule[1])
                rectify(update,rules)
    return update

corrected = []
for update in incorrect_updates:
    working_copy = [x for x in update]
    corrected.append(rectify(working_copy,rules))
    
print(sum([update[int(len(update)/2)] for update in corrected]))
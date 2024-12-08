import numpy as np
numbers = [[int(line.split()[0][:-1])] + [[int(x) for x in line.strip('\n').split()[1:]]] for line in open('input')]

def eval_row(row):
    target = row[0]
    row = row[1]
    spots = len(row) - 1
    trials = 3**(spots)
    schema = [np.base_repr(attempt,base=3).zfill(spots) for attempt in range(trials)]
    
    for trial in schema:
        total_trial = 0
        for i in range(len(row)):
            if i == 0:
                total_trial += row[i]
            else:
                if trial[i-1] == '0':
                    total_trial += row[i]
                elif trial[i-1] == '1':
                    total_trial *= row[i]
                elif trial[i-1] == '2':
                    total_trial = int(str(total_trial)+str(row[i]))
                    
        if total_trial == target:
            return target
        else:
            continue
    return False

#0 = +
#1 = *
#2 = ||
calibration_result = 0
runs = len(numbers)
for n,row in enumerate(numbers):
    calibration_result += eval_row(row)
    print(f'{n+1}/{runs}')

print(calibration_result)

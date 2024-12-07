numbers = [[int(line.split()[0][:-1])] + [[int(x) for x in line.strip('\n').split()[1:]]] for line in open('input')]

def eval_row(row):
    target = row[0]
    row = row[1]
    spots = len(row) - 1
    trials = 2**(spots)
    schema = [bin(attempt)[2:].zfill(spots) for attempt in range(trials)]
    
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
        if total_trial == target:
            return target
        else:
            continue
    return False

#0 = +
#1 = *
calibration_result = 0
for row in numbers:
    calibration_result += eval_row(row)

print(calibration_result)
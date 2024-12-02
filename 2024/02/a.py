import numpy as np

reports = []
safes = []
with open('input') as f:
    for line in f:
        report = [int(n) for n in line.split()]
        report_diff = np.diff(report)
        if (all(x>0 for x in report_diff) and max(report_diff) <= 3) or (all(x<0 for x in report_diff) and min(report_diff) >= -3):
            safes.append(1)
        else:
            safes.append(0)
            
print(sum(safes))
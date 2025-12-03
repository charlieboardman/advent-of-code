file_contents = open('input.txt').read()
str_ranges = file_contents.split(',')

def build_ids_list(str_range):
    a,b = [int(x) for x in str_range.split('-')]
    return list(range(a,b+1))

master_list = []

for r in str_ranges:
    master_list += build_ids_list(r)
    
total = 0

'''A string is made up of a repeated pattern if the original string
is found somewhere within the original string concatenated with itself
'''

for num in master_list:
    concat_num = 2*str(num)
    trimmed_concat_num = concat_num[1:-1]
    if trimmed_concat_num.find(str(num)) != -1: #find returns -1 if string not found
        total += num
        
print(total)
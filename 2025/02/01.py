file_contents = open('input.txt').read()
str_ranges = file_contents.split(',')

def build_ids_list(str_range):
    a,b = [int(x) for x in str_range.split('-')]
    return list(range(a,b+1))

master_list = []

for r in str_ranges:
    master_list += build_ids_list(r)

def id_is_invalid(product_id: str):
    if product_id[:len(product_id)//2] == product_id[len(product_id)//2:]:
        return True
    else:
        return False
    
total = 0    

for i in master_list:
    if id_is_invalid(str(i)):
        total += i
        
print(total)
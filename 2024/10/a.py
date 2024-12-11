from copy import deepcopy

trailmap = [[int(c) if c.isnumeric() else '.' for c in row.strip('\n')] for row in open('input')]

#Assign peak IDs
new_nodes = []
peak_id = 0
for i,row in enumerate(trailmap):
    for j,n in enumerate(row):
        if n == 9: #9s are peaks
            new_nodes.append({'i':i,'j':j,'lvl':9,'IDs':[peak_id]})
            peak_id += 1
    
#Start to search levels
level_search = 8 #start with one below peaks
i_max = len(trailmap)-1
j_max = len(trailmap[0])-1
while level_search >= 0:
    prev_nodes = deepcopy(new_nodes)
    new_nodes = []
    for prev_node in prev_nodes:
        #print(prev_node)
        IDs = prev_node['IDs']
        i_up, i_down, i = prev_node['i']-1, prev_node['i']+1, prev_node['i']
        j_left, j_right, j = prev_node['j']-1, prev_node['j']+1, prev_node['j']
        
        #Search up
        if i_up >= 0 and trailmap[i_up][j] == level_search: #If the spot adjacent up to this node is th
            for n in new_nodes:
                if n['i'] == i_up and n['j'] == j:
                    n['IDs'] += deepcopy(IDs)
                    break           
            else:
                new_nodes.append({'i':i_up,'j':j,'lvl':level_search,'IDs':deepcopy(IDs)})
            
        #Search down
        if i_down <= i_max and trailmap[i_down][j] == level_search:
            for n in new_nodes:
                if n['i'] == i_down and n['j'] == j:
                    n['IDs'] += deepcopy(IDs)
                    break
            else:
                new_nodes.append({'i':i_down,'j':j,'lvl':level_search,'IDs':deepcopy(IDs)})
        
        #Search right
        if j_right <= j_max and trailmap[i][j_right] == level_search:
            for n in new_nodes:
                if n['i'] == i and n['j'] == j_right:
                    n['IDs'] += deepcopy(IDs)
                    break
            else:
                new_nodes.append({'i':i,'j':j_right,'lvl':level_search,'IDs':deepcopy(IDs)})
            
        #Search left
        if j_left >= 0 and trailmap[i][j_left] == level_search:
            for n in new_nodes:
                if n['i'] == i and n['j'] == j_left:
                    n['IDs'] += deepcopy(IDs)
                    break
            else:
                new_nodes.append({'i':i,'j':j_left,'lvl':level_search,'IDs':deepcopy(IDs)})
    level_search -= 1
    
for node in new_nodes:
    node['IDs'] = list(set(node['IDs']))

new_nodes = sorted(new_nodes, key=lambda x: (x['i'], x['j']))
score = sum([len(x['IDs']) for x in new_nodes])
print(score)
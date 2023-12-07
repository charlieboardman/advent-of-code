with open('input.txt','r') as input_doc:
    lines = input_doc.readlines()
    times = [int(x) for x in lines[0].split(':')[1].split()]
    record_distances = [int(x) for x in lines[1].split(':')[1].split()]
    
winning_button_presses = []

num_races = len(record_distances)
winners_by_race = []

for i in range(num_races):
    distances = []
    for j in range(times[i]+1):
        dist_traveled = j * (times[i] - j)
        distances.append(dist_traveled)

    winners = [d for d in distances if d > record_distances[i]]

    winners_by_race.append(winners)

num_winners = [len(x) for x in winners_by_race]

prod = 1
for k in range(len(num_winners)):
    prod *= num_winners[k]
    
print(prod)
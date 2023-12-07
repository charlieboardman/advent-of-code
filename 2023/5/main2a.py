#Destination, source, rang

from time import time

with open('input.txt','r') as input_file:
    lines = input_file.readlines()

#Establish the seeds
seeds_and_ranges = [int(x) for x in lines[0].split(':')[1].split()]

seeds_with_ranges = []

for i in range(0,len(seeds_and_ranges),2):
    seeds_with_ranges.append((seeds_and_ranges[i],seeds_and_ranges[i+1]))
    
seeds_with_ranges = sorted(seeds_with_ranges)

def process_map(x,key_phrase):

    map_lines = []

    #Get the line starting the map for this key phrase
    for i in range(len(lines)):
        if lines[i].strip('\n') == key_phrase:
            i += 1
            break
        
    #Get the map lines under the key phrase
    while i < len(lines) and lines[i] != '\n':
        map_lines.append([int(x) for x in lines[i].split()])
        i += 1

    for map_line in map_lines:
        destination_start = map_line[0]
        source_start = map_line[1]
        rang = map_line[2]
        if x in range(source_start,source_start+rang):
            y = destination_start + (x - source_start)
            return y
                
    y = x
    return y

def establish_map(key_phrase):
    
    map_lines = []

    #Get the line starting the map for this key phrase
    for i in range(len(lines)):
        if lines[i].strip('\n') == key_phrase:
            i += 1
            break
        
    #Get the map lines under the key phrase
    while i < len(lines) and lines[i] != '\n':
        map_lines.append([int(x) for x in lines[i].split()])
        i += 1
        
    return map_lines

maps = []

#Source, rang, destination
seed_to_soil_map = establish_map('seed-to-soil map:')
for i in range(len(seed_to_soil_map)):
    seed_to_soil_map[i] = [seed_to_soil_map[i][1],seed_to_soil_map[i][2],seed_to_soil_map[i][0]]
seed_to_soil_map = sorted(seed_to_soil_map)
maps.append(seed_to_soil_map)

soil_to_fertilizer_map = establish_map('soil-to-fertilizer map:')
for i in range(len(soil_to_fertilizer_map)):
    soil_to_fertilizer_map[i] = [soil_to_fertilizer_map[i][1],soil_to_fertilizer_map[i][2],soil_to_fertilizer_map[i][0]]
soil_to_fertilizer_map = sorted(soil_to_fertilizer_map)
maps.append(soil_to_fertilizer_map)

fertilizer_to_water_map = establish_map('fertilizer-to-water map:')
for i in range(len(fertilizer_to_water_map)):
    fertilizer_to_water_map[i] = [fertilizer_to_water_map[i][1],fertilizer_to_water_map[i][2],fertilizer_to_water_map[i][0]]
fertilizer_to_water_map = sorted(fertilizer_to_water_map)
maps.append(fertilizer_to_water_map)

water_to_light_map = establish_map('water-to-light map:')
for i in range(len(water_to_light_map)):
    water_to_light_map[i] = [water_to_light_map[i][1],water_to_light_map[i][2],water_to_light_map[i][0]]
water_to_light_map = sorted(water_to_light_map)
maps.append(water_to_light_map)
    
light_to_temperature_map = establish_map('light-to-temperature map:')
for i in range(len(light_to_temperature_map)):
    light_to_temperature_map[i] = [light_to_temperature_map[i][1],light_to_temperature_map[i][2],light_to_temperature_map[i][0]]
light_to_temperature_map = sorted(light_to_temperature_map)
maps.append(light_to_temperature_map)
    
temperature_to_humidity_map = establish_map('temperature-to-humidity map:')
for i in range(len(temperature_to_humidity_map)):
    temperature_to_humidity_map[i] = [temperature_to_humidity_map[i][1],temperature_to_humidity_map[i][2],temperature_to_humidity_map[i][0]]
temperature_to_humidity_map = sorted(temperature_to_humidity_map)
maps.append(temperature_to_humidity_map)
    
humidity_to_location_map = establish_map('humidity-to-location map:')
for i in range(len(humidity_to_location_map)):
    humidity_to_location_map[i] = [humidity_to_location_map[i][1],humidity_to_location_map[i][2],humidity_to_location_map[i][0]]
humidity_to_location_map = sorted(humidity_to_location_map)
maps.append(humidity_to_location_map)

def process(_map,value):
    
    if _map[0][0] != 0:
        _map.insert(0,[0,_map[0][0],0])
    
    smallest = _map[0][0]
    
    for line in _map:
        if value < smallest:
            return value
        
        if value >= line[0] + line[1]: #This means it's not on this line 
            continue
        else:
            return line[2] + value - line[0]        
    return value

def seed_to_location(seed):
    soil = process(seed_to_soil_map,seed)
    fertilizer = process(soil_to_fertilizer_map,soil)
    water = process(fertilizer_to_water_map,fertilizer)
    light = process(water_to_light_map,water)
    temperature = process(light_to_temperature_map,light)
    humidity = process(temperature_to_humidity_map,temperature)
    location = process(humidity_to_location_map,humidity)
    return location

#locations_by_seed = [seed_to_location(seed) for seed in seeds]

minimum_location = seed_to_location(seeds_with_ranges[0][0]) #Initialize
counter = 0

start_time = time()

for x in seeds_with_ranges:
    for y in range(x[1]):
        location = seed_to_location(x[0]+y)
        if location < minimum_location:
            minimum_location = location
        counter += 1
        if counter%100000 == 0:
            percent = 100*counter/1809081164
            formatted = '{0:.2f}'.format(percent)
            elapsed = (time()-start_time)
            rate = '{0:.6f}'.format(percent/elapsed)
            print(f'{formatted}% complete, rate {rate}%/s')
            

print(minimum_location)

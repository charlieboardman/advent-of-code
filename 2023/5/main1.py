#Destination, source, rang

with open('input.txt','r') as input_file:
    lines = input_file.readlines()

seeds = [int(x) for x in lines[0].split(':')[1].split()]

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

def seed_to_soil(_input):
    
    key_phrase = 'seed-to-soil map:'
    
    return process_map(_input,key_phrase)

def soil_to_fertilizer(_input):
    
    key_phrase = 'soil-to-fertilizer map:'
    
    return process_map(_input,key_phrase)

def fertilizer_to_water(_input):
    
    key_phrase = 'fertilizer-to-water map:'
    
    return process_map(_input,key_phrase)

def water_to_light(_input):
    
    key_phrase = 'water-to-light map:'
    
    return process_map(_input,key_phrase)

def light_to_temperature(_input):
    
    key_phrase = 'light-to-temperature map:'
    
    return process_map(_input,key_phrase)

def temperature_to_humidity(_input):
    
    key_phrase = 'temperature-to-humidity map:'
    
    return process_map(_input,key_phrase)

def humidity_to_location(_input):
    
    key_phrase = 'humidity-to-location map:'
    
    return process_map(_input,key_phrase)

def seed_to_location(seed):
    soil = seed_to_soil(seed)
    fertilizer = soil_to_fertilizer(soil)
    water = fertilizer_to_water(fertilizer)
    light = water_to_light(water)
    temperature = light_to_temperature(light)
    humidity = temperature_to_humidity(temperature)
    location = humidity_to_location(humidity)
    return location

locations_by_seed = [seed_to_location(seed) for seed in seeds]

print(min(locations_by_seed))

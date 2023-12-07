with open('input.txt','r') as game_data:
    games = game_data.readlines()
    
    total = 0
    
    for game in games:
        
        max_red = 0
        max_blue = 0
        max_green = 0
        
        game_number = int(game.split(':')[0].split()[1])
        samples_data = game.split(': ')[1]
        samples = samples_data.split('; ')
        
        for sample in samples:
            data = sample.split(', ')
            for cubes in data:
                quantity = int(cubes.split()[0])
                color = cubes.split()[1]
                
                if color.strip('\n') == 'red':
                    if quantity > max_red:
                        max_red = quantity
                        
                if color.strip('\n') == 'blue':
                    if quantity > max_blue:
                        max_blue = quantity
                        
                if color.strip('\n') == 'green':
                    if quantity > max_green:
                        max_green = quantity
        
        if max_red <= 12 and max_blue <= 14 and max_green <= 13:
            total += game_number
            
print(total)
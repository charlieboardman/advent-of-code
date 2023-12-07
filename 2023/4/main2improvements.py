with open ('input.txt','r') as input_file:
    cards = input_file.readlines()
    
    
games = [[[int(x) for x in card.split('|')[0].split(':')[1].split()],[int(x) for x in card.split('|')[1].split()]] for card in cards]

my_winners = [[n for n in y if n in x] for x,y in games]

my_winners_w_copies = [[x,1] for x in my_winners]

for i in range(len(my_winners)):
    winnings = len(my_winners_w_copies[i][0])
    copies = my_winners_w_copies[i][1]
    for n in range(copies): #You have to do this once for every copy you have
        for j in range(winnings):
            my_winners_w_copies[i+j+1][1] += 1

print(sum([x[1] for x in my_winners_w_copies]))

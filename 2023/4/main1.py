with open ('input2.txt','r') as input:
    cards = input.readlines()
    
# winning_numbers = [card.split('|')[0].split(':')[1].split() for card in cards]
# my_numbers = [card.split('|')[1].split() for card in cards]

# winning_numbers = [[int(x) for x in card.split('|')[0].split(':')[1].split()] for card in cards]
# my_numbers = [[int(x) for x in card.split('|')[1].split()] for card in cards]


games = [[[int(x) for x in card.split('|')[0].split(':')[1].split()],[int(x) for x in card.split('|')[1].split()]] for card in cards]

my_winners = [[n for n in y if n in x] for x,y in games]

scores = [2**(len(x)-1) for x in my_winners if len(x) != 0]

score = sum(scores)

print(score)
with open('input.txt','r') as input_file:
    lines = input_file.readlines()

lines = [line.strip('\n') for line in lines]

hands = [[x.split()[0],int(x.split()[1])] for x in lines]

hands_broken_down = []


card_str= {'J':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'Q':10,'K':11,'A':12}

def optimize_hand(hand):
        
        if 'J' in hand[0]:
            best_swap_card = '2'
            best_type = 'G'
            for swap_card in list(card_str.keys())[1::]:
                swap_hand = [''.join([c if c != 'J' else swap_card for c in hand[0]]),hand[1]]
                hand_type = evaluate_hand(swap_hand)
                if hand_type < best_type:
                    best_type = hand_type
                    best_swap_card = swap_card
                    best_hand = swap_hand
            return [[hand[0],best_hand[0]],hand[1]],best_type
        
        else:
            best_type = evaluate_hand(hand)
            return [[hand[0],hand[0]],hand[1]],best_type
            
            
def evaluate_hand(hand):
#This determines the type
    
    #After this, it goes [hand,bid,breakdown]
    breakdown = [[x,hand[0].count(x)] for x in hand[0]]
    breakdown = [x+str(y) for x,y in breakdown]
    breakdown = list(set(breakdown))
    breakdown = [[x[0],int(x[1])] for x in breakdown]
    
    length_breakdown = len(breakdown)

    if length_breakdown == 1: #5 of a kind
        return 'A'
    
    if length_breakdown == 2: #Full house or 4 or a kind:
        if breakdown[0][1] in range(2,4): #if 2 or 3, full house
            return 'C'
        
        else: #4 of a kind
            return 'B'
        
    
    if length_breakdown == 3: #3 of a kind or 2 pair
        if 3 in [x[1] for x in breakdown]: #3 of a kind
            return 'D'
        
        else: #2 pair
            return 'E'
            
    if length_breakdown == 4: #2 of a kind
        return 'F'
            
    if length_breakdown == 5: #High card
        return 'G'
            
for n,hand in enumerate(hands):
    hand,_type = optimize_hand(hand)
    hand.append(_type)
    hands[n] = hand

A_hands = [hand for hand in hands if hand[2] == 'A']
B_hands = [hand for hand in hands if hand[2] == 'B']
C_hands = [hand for hand in hands if hand[2] == 'C']
D_hands = [hand for hand in hands if hand[2] == 'D']
E_hands = [hand for hand in hands if hand[2] == 'E']
F_hands = [hand for hand in hands if hand[2] == 'F']
G_hands = [hand for hand in hands if hand[2] == 'G']


def compare_hands(hand_a,hand_b): #Returns true if a > b, false if b > a
    n_cards = 5 #5 cards in a hand
    for n in range(n_cards):
        if card_str[hand_a[0][0][n]] > card_str[hand_b[0][0][n]]: #hand_a win
            return True
        
        if card_str[hand_a[0][0][n]] < card_str[hand_b[0][0][n]]: #hand_b win
            return False
        
        else:
            continue
        
def hands_sort(hand_group):
    
    n_hands = len(hand_group)
    n = 0
    
    while n < n_hands - 1:
        if compare_hands(hand_group[n],hand_group[n+1]):
            swap = hand_group[n]
            hand_group[n] = hand_group[n+1]
            hand_group[n+1] = swap
            n = 0
            continue
        n += 1
        
try:
    hands_sort(A_hands)
except:
    pass

try:
    hands_sort(B_hands)
except:
    pass

try:
    hands_sort(C_hands)
except:
    pass

try:
    hands_sort(D_hands)
except:
    pass

try:
    hands_sort(E_hands)
except:
    pass

try:
    hands_sort(F_hands)
except:
    pass    

try:
    hands_sort(G_hands)
except:
    pass

hands_sorted = G_hands + F_hands + E_hands + D_hands + C_hands + B_hands + A_hands

winnings = 0

for rank,hand in enumerate(hands_sorted):
    winnings += (rank+1) * hand[1]
    
print(winnings)
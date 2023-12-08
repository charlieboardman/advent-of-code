with open('input.txt','r') as input_file:
    lines = input_file.readlines()

lines = [line.strip('\n') for line in lines]

hands = [[x.split()[0],int(x.split()[1])] for x in lines]

hands_broken_down = []

for hand in hands:
    breakdown = [[x,hand[0].count(x)] for x in hand[0]]
    breakdown = [x+str(y) for x,y in breakdown]
    breakdown = list(set(breakdown))
    breakdown = [[x[0],int(x[1])] for x in breakdown]
    
    hand.append(breakdown)
    
for hand in hands:
    
    length_breakdown = len(hand[2])
    
    if length_breakdown == 1: #5 of a kind
        hand.append('A')
        continue
    
    if length_breakdown == 2: #Full house or 4 or a kind:
        if hand[2][0][1] in range(2,4): #if 2 or 3, full house
            hand.append('C')
            continue
        else: #4 of a kind
            hand.append('B')
            continue
    
    if length_breakdown == 3: #3 of a kind or 2 pair
        if 3 in [x[1] for x in hand[2]]: #3 of a kind
            hand.append('D')
            continue
        else: #2 pair
            hand.append('E')
            continue
    
    if length_breakdown == 4: #2 of a kind
        hand.append('F')
        continue
    
    if length_breakdown == 5: #High card
        hand.append('G')
        continue
    
A_hands = [hand for hand in hands if hand[3] == 'A']
B_hands = [hand for hand in hands if hand[3] == 'B']
C_hands = [hand for hand in hands if hand[3] == 'C']
D_hands = [hand for hand in hands if hand[3] == 'D']
E_hands = [hand for hand in hands if hand[3] == 'E']
F_hands = [hand for hand in hands if hand[3] == 'F']
G_hands = [hand for hand in hands if hand[3] == 'G']

card_str= {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}

def compare_hands(hand_a,hand_b): #Returns true if a > b, false if b > a
    n_cards = 5 #5 cards in a hand
    for n in range(n_cards):
        if card_str[hand_a[0][n]] > card_str[hand_b[0][n]]: #hand_a win
            return True
        
        if card_str[hand_a[0][n]] < card_str[hand_b[0][n]]: #hand_b win
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
        
        
hands_sort(A_hands)
hands_sort(B_hands)
hands_sort(C_hands)
hands_sort(D_hands)
hands_sort(E_hands)
hands_sort(F_hands)
hands_sort(G_hands)

hands_sorted = G_hands + F_hands + E_hands + D_hands + C_hands + B_hands + A_hands

winnings = 0

for rank,hand in enumerate(hands_sorted):
    winnings += (rank+1) * hand[1]
    
print(winnings)
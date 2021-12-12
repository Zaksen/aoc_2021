with open('input.txt', 'r') as f:
    drawn = [int(x.rstrip()) for x in f.readline().split(',')]
    cards = []
    while f.readline():
        card = []
        for i in range(5):
            card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
        cards.append(card)


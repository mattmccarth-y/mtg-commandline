import random

def shuffle(decklist):
    random.shuffle(decklist)
    return decklist

def drawcards(hand, library, num=1):
    for i in range(num):
        hand.append(library[0])
        del(library[0])
    return hand, library

def bottomcards(hand, library, cards):
    cards = list(map(int, cards))
    cards.sort()
    print(cards)
    for i in range(1,len(cards)+1):
        print(hand)
        library.append(hand[cards[i-1]-i])
        del(hand[cards[i-1]-i])
    return hand, library

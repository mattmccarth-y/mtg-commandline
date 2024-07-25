import os
import random
import libraryactions
import prints

def mulligans(deck, decklist, keep=False, mull=0, remove=[]):
    library = decklist
    while keep == False:
        os.system("clear")
        hand = []
        print("### DRAW ###\n")
        libraryactions.shuffle(library)
        hand, library = libraryactions.drawcards(hand, library, num=7)
        prints.printhand(deck, hand)
        if input("Keep hand (y or n)") == ("y" or "Y"):
            keep = True
        else:
            keep = False
            mull += 1
            libraryactions.bottomcards(hand, library, cards=[1,2,3,4,5,6,7])
    if mull > 0:
        print(f"Choose {mull} cards to bottom")
        for i in range(mull):
            remove.append(input())
        hand, library = libraryactions.bottomcards(hand, library, remove)
    return hand, library

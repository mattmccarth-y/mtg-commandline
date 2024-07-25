import os
import libraryactions
import prints

def taketurn(deck, hand, library, field, turnum, passturn=False):
    if turnum != 1:
        hand, library = libraryactions.drawcards(hand, library)
    while passturn == False:
        os.system("clear")
        print(f"### TURN {turnum} ###\n")
        prints.printfield(deck, field)
        prints.printhand(deck, hand)
        played = input("Choose card to play (hit enter to pass)\n")
        if played == "":
            passturn = True
            break
        elif played == "exit":
            turnum = 54
            break
        hand, field = playcards(hand, field, played)
    turnum += 1
    return hand, library, field, turnum

def playcards(hand, field, played):
    played = list(map(int, played))
    played.sort()
    for i in range(1,len(played)+1):
        field.append(hand[played[i-1]-i])
        del(hand[played[i-1]-i])
    return hand, field

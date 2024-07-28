import os
import libraryactions
import prints

def taketurn(deck, hand, library, field, grave, turnum, passturn=False):
    if turnum != 1:
        hand, library = libraryactions.drawcards(hand, library)
    while passturn == False:
        os.system("clear")
        print(f"### TURN {turnum} ###\n")
        prints.printfield(deck, field)
        prints.printgrave(deck, grave)
        prints.printhand(deck, hand)
        played = input("Choose card to play (hit enter to pass)\n")
        if played == "":
            passturn = True
            break
        elif played == "exit":
            turnum = 54
            break
        hand, field, grave = playcards(deck, hand, field, grave, played)
    turnum += 1
    return hand, library, field, grave, turnum

def playcards(deck, hand, field, grave, played):
    played = list(map(int, played))
    played.sort()
    for i in range(1,len(played)+1):
        types = deck.get("cards").get(hand[played[i-1]-i]).get("type")
        if ("Creature" in types) or ("Land" in types) or ("Artifact" in types) or ("Enchantment" in types) or ("Planeswalker" in types) or ("Battle" in types):
            field.append(hand[played[i-1]-i])
            del(hand[played[i-1]-i])
        else:
            grave.append(hand[played[i-1]-i])
            del(hand[played[i-1]-i])
    return hand, field, grave

import utils

def printhand(deck, hand):
    print("### HAND ###")
    num = 1
    for card in hand:
        types = deck.get("cards").get(card).get("type")
        print(f"{num:<2} - {card:<25} ({utils.list2string(types)})")
        num += 1
    print("############\n")
    return

def printfield(deck, field):
    print("### BATTLEFIELD ###")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Creature" in types:
            print(f"{card:<23} ({utils.list2string(types)})")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Land" in types:
            print(f"{card:<23} ({utils.list2string(types)})")
    print("###################\n")
    return

def printlibrary(deck, library):
    print("### LIBRARY ###")
    for card in library:
        types = deck.get("cards").get(card).get("type")
        print(f"{card:<23} ({utils.list2string(types)})")
    print("###############\n")
    return

def printdeck(deck, decklist):
    print("### DECK ###")
    for card in decklist:
        types = deck.get("cards").get(card).get("type")
        print(f"{card:<23} ({utils.list2string(types)})")
    print("############\n")
    return

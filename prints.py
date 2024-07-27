def printhand(deck, hand):
    print("### HAND ###")
    num = 1
    for card in hand:
        print(f"{num:<2} - {card:<25} ({deck.get('cards').get(card).get('type')})")
        num += 1
    print("############\n")
    return

def printfield(deck, field):
    print("### BATTLEFIELD ###")
    for card in field:
        if deck.get("cards").get(card).get("type") == "Creature":
            print(f"{card:<23} ({deck.get('cards').get(card).get('type')})")
    for card in field:
        if deck.get("cards").get(card).get("type") == "Land":
            print(f"{card:<23} ({deck.get('cards').get(card).get('type')})")
    print("###################\n")
    return

def printlibrary(deck, library):
    print("### LIBRARY ###")
    for card in library:
        print(f"{card:<23} ({deck.get('cards').get(card).get('type')})")
    print("###############\n")
    return

def printdeck(deck, decklist):
    print("### DECK ###")
    for card in decklist:
        print(f"{card:<23} ({deck.get('cards').get(card).get('type')})")
    print("############\n")
    return

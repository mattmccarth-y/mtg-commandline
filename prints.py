import utils

def printhand(deck, hand):
    print(f"{' HAND ':#^75}")
    num = 1
    for card in hand:
        types = deck.get("cards").get(card).get("type")
        subtypes = deck.get("cards").get(card).get("subtype")
        cost = deck.get("cards").get(card).get("cost", " ")
        if subtypes == None:
            print(f"{num:<2} | {cost:^10} | {card:^30} | ({utils.list2string(types)})")
        else:
            print(f"{num:<2} | {cost:^10} | {card:^30} | ({utils.list2string(types)} - {utils.list2string(subtypes)})")
        num += 1
    print(f"{'######':#^75}\n")
    return

def printfield(deck, field):
    print(f"{' BATTLEFIELD ':#^75}")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Creature" in types:
            subtypes = deck.get("cards").get(card).get("subtype")
            produces = deck.get("cards").get(card).get("produces", " ")
            if subtypes == None:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)})")
            else:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Planeswalker" in types:
            subtypes = deck.get("cards").get(card).get("subtype")
            produces = deck.get("cards").get(card).get("produces", " ")
            if subtypes == None:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)})")
            else:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Enchantment" in types:
            subtypes = deck.get("cards").get(card).get("subtype")
            produces = deck.get("cards").get(card).get("produces", " ")
            if subtypes == None:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)})")
            else:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Artifact" in types:
            subtypes = deck.get("cards").get(card).get("subtype")
            produces = deck.get("cards").get(card).get("produces", " ")
            if subtypes == None:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)})")
            else:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    for card in field:
        types = deck.get("cards").get(card).get("type")
        if "Land" in types:
            subtypes = deck.get("cards").get(card).get("subtype")
            produces = deck.get("cards").get(card).get("produces", " ")
            if subtypes == None:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)})")
            else:
                print(f"{produces:^23} {card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    print(f"{'#############':#^75}\n")
    return

def printgrave(deck, grave):
    print(f"{' GRAVEYARD ':#^75}")
    for card in grave:
        types = deck.get("cards").get(card).get("type")
        subtypes = deck.get("cards").get(card).get("subtype")
        if subtypes == None:
            print(f"{card:^30} ({utils.list2string(types)})")
        else:
            print(f"{card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    print(f"{'###########':#^75}\n")
    return

def printlibrary(deck, library):
    print(f"{' LIBRARY ':#^75}")
    for card in library:
        types = deck.get("cards").get(card).get("type")
        subtypes = deck.get("cards").get(card).get("subtype")
        if subtypes == None:
            print(f"{card:^30} ({utils.list2string(types)})")
        else:
            print(f"{card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    print(f"{'#########':#^75}\n")
    return

def printdeck(deck, decklist):
    print(f"{' DECK ':#^75}")
    for card in decklist:
        types = deck.get("cards").get(card).get("type")
        subtypes = deck.get("cards").get(card).get("subtype")
        if subtypes == None:
            print(f"{card:^30} ({utils.list2string(types)})")
        else:
            print(f"{card:^30} ({utils.list2string(types)} - {utils.list2string(subtypes)})")
    print(f"{'######':#^75}\n")
    return

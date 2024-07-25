import json

def deckopener(deckfile):
    with open(deckfile, 'r') as df:
        deck = json.load(df)
    return deck

def dict2list(deck):
    cards = deck.get("cards")
    decklist = []
    for each in cards:
        for i in range(cards.get(each).get("amount")):
            decklist.append(cards.get(each).get("name"))
    return decklist

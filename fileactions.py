import json

def deckopener(deckfile):
    with open(deckfile, 'r') as df:
        deck = json.load(df)
    return deck

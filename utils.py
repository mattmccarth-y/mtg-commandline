def dict2list(deck):
    cards = deck.get("cards")
    decklist = []
    for each in cards:
        for i in range(cards.get(each).get("amount")):
            decklist.append(cards.get(each).get("name"))
    return decklist

def list2string(changelist):
    if type(changelist) == list:
        return " ".join(map(str, changelist))
    else:
        return changelist

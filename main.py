import sys
import fileactions
import libraryactions
import utils
import pregame
import turns

#open the decklist
deck = fileactions.deckopener(sys.argv[1])
decklist = utils.dict2list(deck)

#resolve mulligans
hand, library = pregame.mulligans(deck, decklist)

#start game
field = []
grave = []
turnum = 1
while True:
    hand, library, field, grave, turnum = turns.taketurn(deck, hand, library, field, grave, turnum)
    if turnum == 55:
        break

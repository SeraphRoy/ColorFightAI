#!/usr/bin/env python

import colorfight
import random

if __name__ == '__main__':
    g = colorfight.Game()
    g.JoinGame('hahaAI')

    while True:
        for x in range(g.width):
            for y in range(g.height):
                c = g.GetCell(x,y)
                if c.owner == g.uid:
                    d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
                    cc = g.GetCell(x+d[0], y+d[1])
                    if cc != None:
                        if cc.owner != g.uid:
                            g.AttackCell(x+d[0], y+d[1])
                            g.Refresh()

oppoCells = []
oppoPlays = []
myCells = []
myPlays = []
MAX_DEPTH = 10
WORST_PLAY = 0
BEST_PLAY = 1000000
currentScore = 0
def myPlay( depth ):
    result = Result()
    if depth >= MAX_DEPTH:
        result = max( [ ifPlay( play, 'my' ) for play in myPlays ] )
    else:
        results = []
        for play in myPlays:
            playLocal( play )
            results.append( oppoPlay( depth + 1 ) )
            revertPlay( play )
            
        result = max( results )
    if ( play( result ) == True ):
        updateInfo()
    return result

def oppoPlay( ):
    result = Result()
    if depth >= MAX_DEPTH:
        result = min( [ ifPlay( play, 'oppo' ) for play in oppoPlays ] )
    else:
        results = []
        for play in oppoPlays:
            playLocal( play )
            results.append( myPlay( depth + 1 ) )
            revertPlay( play )
            
        result = max( results )
    if ( play( result ) == True ):
        updateInfo()
    return result

def ifPlay( play, whosePlay ):
    if whosePlay == 'my':
        return currenetScore + playScore( play )
    else:
        return currentScore - playScore( play )

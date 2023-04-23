from catanatron import Game, RandomPlayer, Color
from fortomm import PlayerE

from catanatron_core.catanatron.players.weighted_random import WeightedRandomPlayer

from collections import Counter

import random

import multiprocessing

playerDict = {
    Color.RED: 0,
    Color.BLUE: 1,
    Color.WHITE: 2,
    Color.ORANGE: 3,
}


players = [
    WeightedRandomPlayer(Color.RED),
    PlayerE(Color.BLUE),
    PlayerE(Color.WHITE),
    PlayerE(Color.ORANGE),
]

NumberOfGames = 50


firstPlayersCopy = {
    Color.BLUE: players[1].copyData(),
    Color.WHITE: players[2].copyData(),
    Color.ORANGE: players[3].copyData(),
}



BestPlayer = None
BestScore = 0



for generations in range(100):
    victory = []

    for games in range(NumberOfGames):

        game = Game(players)
        val = game.play()
        victory.append(val)
        
    c = dict(Counter(victory))
    print(generations)

    # find the ratio of wins
    for key in c:
        c[key] = int(c[key] / NumberOfGames * 100)

    print(c) 

    # find the best player
    for key in c:
        if c[key] > BestScore and key != Color.RED:
            BestScore = c[key]
            BestPlayer = players[playerDict[key]]
            print("New Best Player: ", BestPlayer, " with score: ", BestScore)

    # mutate the best player

    # extend = []
    # for i in c:
    #     if i == Color.RED or not i:
    #         continue
    #     extend = extend + [i] * c[i]

    # # make a random pick from the list extend
    # pick = random.choice(extend)
    # players[playerDict[pick]].mutate()
    
    # sort the list by the number of wins
    # st = sorted(c.items(), key=lambda x: x[1], reverse=True)

    temp = c.pop(Color.RED, None)
    temp = c.pop(None, None)
    st = sorted(c.items(), key=lambda x: x[1], reverse=True)
    players[1].setData(players[playerDict[st[0][0]]].copyData())
    players[playerDict[st[0][0]]].mutate()
    players[2].setData(players[playerDict[st[0][0]]].copyData())
    players[playerDict[st[1][0]]].mutate()
    players[3].setData(players[playerDict[st[1][0]]].copyData())

    # for key in c:
    #     # if Color.RED == key:
    #     #     continue
    #     if c[key] < 0.5 and key != Color.RED:
    #         try:
    #             players[playerDict[key]].mutate()
    #         except:
    #             print("Error: ", key)



print(BestPlayer.WEIGHTS_BY_ACTION_TYPE)
print(BestScore)

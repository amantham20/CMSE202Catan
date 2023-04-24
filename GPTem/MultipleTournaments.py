from catanatron import Game, RandomPlayer, Color
from fortomm import PlayerE

from catanatron_core.catanatron.players.weighted_random import WeightedRandomPlayer

from collections import Counter

# import multiprocessing as mp
# import multiprocessing
# import threading
# import concurrent.futures

# import logging

import csv

import logging

logging.basicConfig(filename='tournament.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

import pickle

tournament_results = []
best_players = []

NUMBER_OF_TOURNAMENTS = 1
NumberOfGames = 100
GENERATIONS = 50
ADDITIONALGAMES = 150


def PrintTheOrder(items: dict):
    pos = 0
    for i in sorted(items, key=items.get, reverse=True):
        print(f"\033[1;32m  ({pos}) {i} : {items[i]} \033[00m")
        logging.info(f"  ({pos}) {i} : {items[i]}")
        pos += 1
        
def RunAgainstWeighted(players, NumberOfGames):
    victory = []
    for __ in range(NumberOfGames):
        game = Game(players)
        val = game.play()
        victory.append(val)
    tempC = dict(Counter(victory))
    for key in tempC:
        tempC[key] = int(tempC[key] / NumberOfGames * 100)
    PrintTheOrder(tempC)
    # return
    
    
def SavePlayerScores(Scores):
    with open('player_scores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Generation'] + [f'Player {i.color}' for i in players])
        for i in range(GENERATIONS):
            writer.writerow([i+1] + Scores[i])
            
            
def ComputeWinRate(Counter):
    for key in Counter:
        Counter[key] = int(Counter[key] / NumberOfGames * 100)
    

for tournament in range(NUMBER_OF_TOURNAMENTS):
        
    playerDict = {
        Color.RED: 0,
        Color.BLUE: 1,
        Color.WHITE: 2,
        Color.ORANGE: 3,
    }

    players = [
        WeightedRandomPlayer(Color.RED),
        PlayerE(Color.BLUE, printout=True),
        PlayerE(Color.WHITE, printout=True),
        PlayerE(Color.ORANGE, printout=True),
    ]

    firstPlayersCopy = [None, players[1].copyData(), players[2].copyData(), players[3].copyData()]

    BestPlayer = None
    BestScore = 0
    
    player_scores = [[0]*len(players) for _ in range(GENERATIONS)]

    for generations in range(GENERATIONS):
        
        victory = []

        for games in range(NumberOfGames):
            game = Game(players)
            val = game.play()
            victory.append(val)
            
        c = dict(Counter(victory))
        print(generations)

        # for key in c:
        #     c[key] = int(c[key] / NumberOfGames * 100)
        ComputeWinRate(c)

        print(c, " Score of weighted random:", c[Color.RED])
        
        
        for _, player in enumerate(players):
            player_scores[generations][playerDict[player.color]] = c.get(player.color, 0)

        # find the best player
        logging.debug(f"Generation {generations}, tournament {tournament}: {c}  {c[Color.RED]}")
        for key in c:
            if c[key] > BestScore and key != Color.RED:
                BestScore = c[key]
                BestPlayer = players[playerDict[key]].copyData()
                print("New Best Player: ", BestPlayer, " with score: ", BestScore)
                logging.debug(f"New Best Player: {BestPlayer}, score: {BestScore}")
                print("********* The Best against WR *********")
                RunAgainstWeighted([ players[playerDict[key]], players[0]], NumberOfGames=NumberOfGames)
                print()
                print()
                
        
        if generations % 10 == 0 or c[Color.RED] < 25: 
            for playerForTemp in c:
                if playerForTemp == Color.RED:
                    continue
                if playerForTemp == None:
                    continue
                RunAgainstWeighted([players[playerDict[playerForTemp]], players[0]], NumberOfGames=NumberOfGames)
                print("")
            
            

        # mutate the best player
        temp = c.pop(Color.RED, None)
        temp = c.pop(None, None)
        st = sorted(c.items(), key=lambda x: x[1], reverse=True)
                
        try:
            players[1].setData(players[playerDict[st[0][0]]].copyData())
            players[playerDict[st[0][0]]].mutate()
            players[2].setData(players[playerDict[st[0][0]]].copyData())
            players[playerDict[st[1][0]]].mutate()
            players[3].setData(players[playerDict[st[1][0]]].copyData())
        except:
            print('An exception occurred')
            logging.warning('An exception occurred')

        # mutate the best player
        # extend = []
        # for i in c:
        #     if i == Color.RED or not i:
        #         continue
        #     extend = extend + [i] * c[i]

        # make a random pick from the list extend
        # pick = random.choice(extend)
        # players[playerDict[pick]].mutate()
    
    # make this print orange
    print("\033[1;33m************************** ANALYSIS ************************** \033[00m")
    print("Running for the last itteration of the bots againts the first bots")
    # save the scores of other players
    otherbots = {}
    for i in c:
        # otherbots[i] = c[i]
        otherbots[i] = players[playerDict[i]].copyData()
        

    for bot in otherbots:
        players[0] = PlayerE(Color.RED)
        players[0].setData(otherbots[bot])

        for i in range(1, len(players)):
            players[i].setData(firstPlayersCopy[i])
            
        victory = []
        for games in range(NumberOfGames + ADDITIONALGAMES):
            game = Game(players)
            val = game.play()
            victory.append(val)
            
        c = dict(Counter(victory))
        for key in c:
            c[key] = int(c[key] / (NumberOfGames+ADDITIONALGAMES) * 100)


        print("\n\nbest from last session tournament *****", bot , " =>> RedBOT these weights will be placed in red bots")
        logging.info(f"best from last session tournament ***** {bot} =>> RedBOT these weights will be placed in red bots")
        PrintTheOrder(c)    
        
    for playerForTemp in c:
        if playerForTemp == Color.RED:
            continue
        if playerForTemp == None:
            continue
        RunAgainstWeighted([players[playerDict[playerForTemp]], players[0]], NumberOfGames=NumberOfGames)
        print("")
        
    logging.info(f"Best player's weights: {BestPlayer}, score: {BestScore}")
    
    print("Best player's weights: ", BestPlayer, " score: ", BestScore)
    print("The Best Player's weights will be placed in the red bots")
    players[0] = PlayerE(Color.RED)
    players[0].setData(BestPlayer)

    for i in range(1, len(players)):
        players[i].setData(firstPlayersCopy[i])
        
    victory = []
    for games in range(NumberOfGames):
        game = Game(players)
        val = game.play()
        victory.append(val)
        
    c = dict(Counter(victory))
    
    # for key in c:
    #     c[key] = int(c[key] / NumberOfGames * 100)
    ComputeWinRate(c)
        
    SavePlayerScores(player_scores)
    
    # printing the results form the tournament
    PrintTheOrder(c)
    tournament_results.append(c)

    # store best player
    best_players.append((BestPlayer, BestScore))
    logging.info(f"Tournament {tournament} results: {c}")



# Saving the file data
with open("SavedData/tournament_results.pkl", "wb") as f:
    pickle.dump(tournament_results, f)

with open("SavedData/best_players.pkl", "wb") as f:
    pickle.dump(best_players, f)



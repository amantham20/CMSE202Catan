# CMSE202Catan



Catanatron - Used this existing code to run games of Catan, as well as built off of the basic player class. 

Link - https://github.com/bcollazo/catanatron




Our Goal for this project is to find weights for actions in a Catan Game, aka what kind of move is the best move? And when is this move good or bad compared to other moves?


Our First Approaches to solving this are in the GPTem folder. This approaches were preliminary and didn't really result in too many meaningful conslusions. Some approaches we tried in this code were to play Catan games and mutate the bots who lost, as well as applying selective pressure for genetic programming.




GP 100 Generation Sim contains our Second Approach to the Problem, which was to create generations of bots and have those bots play each other to determine the most "fit" bots, which would then used to create the net generation.

The bots in this simulation contains 12 different weights, which account for the 4 main moves that can be made in Catan (Building a City, Building a Settlement, Buying Development Cards, and Building Roads) in 3 different stages of the game (Early, Mid, and Late)

```python

```

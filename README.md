# CMSE202Catan



Catanatron - Used this existing code to run games of Catan, as well as built off of the basic player class. 

Link - https://github.com/bcollazo/catanatron



Our Goal for this project is to find weights for actions in a Catan Game, aka what kind of move is the best move? And when is this move good or bad compared to other moves. The bot that they have has weights on random values and we wanted to improve this result from the ground up.

Our First Approaches to solving this are in the GPTem folder. This approaches were preliminary and didn't really result in too many meaningful conslusions. Some approaches we tried in this code were to play Catan games and mutate the bots who lost, as well as applying selective pressure for genetic programming.

Our Second Approach can be found in the file GP_100_Generation_Sim, where we created generations of bots and had those bots play each other to determine the most "fit" bots, which would then used to create the next generation.


The bots in this simulation contains 12 different weights, which account for the 4 main moves that can be made in Catan (Building a City, Building a Settlement, Buying Development Cards, and Building Roads) in 3 different stages of the game (Early, Mid, and Late)


To keep this within the realms of CMSE202, we took advantage of **classes** to visualize our data.

Our use of classes focused in the implementation of numpy and matplotlib to run our data through a dictionary fit to our class to create subplots that showed our players.

These subplots contained an aesthetic visualization of the actions that were being done by each player and how many times.

We used this data to determine the best methods of play as well and how to interpret different paths of play.

This also made it much quicker for us to create visuals and determine which players were standing out and why they were, which also made it easier for us to look into both approaches of our own methods.


```python

```

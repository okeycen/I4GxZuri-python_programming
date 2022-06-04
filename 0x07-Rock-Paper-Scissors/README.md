# [Rock-Paper-Scissors]
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

 

# A brief summary:
If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
This program creates a simple version of this game with Python. One player in this version is controlled by the computer and the other player controlled by the user (i.e CPU vs Player). 

Python inbuilt random module  and its choice method is used to randomly select the choice of the computer

list to store all possible options:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".

# Instructions:
When the program is run, ask the user to pick an option between "R", "P" or "S"
If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
Check both player's moves: 
If there is a winner, print the winner, and the program ends. 
If it's a tie (the computer and player pick the same move), restart the game from step 3


# Resources:
How to Play Rock, Paper, Scissors: https://www.youtube.com/watch?v=ND4fd6yScBM

Rock paper scissors - Wikipedia: https://en.wikipedia.org/wiki/Rock_paper_scissors

Introduction to Python Modules: https://www.youtube.com/watch?v=uoVUOTPL9Rw&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=27

Python Random Module: https://www.w3schools.com/python/module_random.asp

Python random choice() function to select a random item from a List and Set: https://pynative.com/python-random-choice/

For Loops: https://www.youtube.com/watch?v=P9sIg93Boso&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=18

While Loops: https://www.youtube.com/watch?v=J8dkgM8Mck0&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=20

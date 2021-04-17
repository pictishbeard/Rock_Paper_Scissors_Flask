from models.player import Player
from models.list_players import *

def play_game(move1, move2):
    if move1 == "Rock" and move2 == "Scissors":
        return f"{list_players.player1} wins by playing {list_players.move1}"

    if move1 == "Scissors" and move2 == "Paper":
        return f"{list_players.player1} wins by playing {list_players.move1}"
    
    if move1 == "Paper" and move2 == "Rock":
        return f"{list_players.player1} wins by playing {list_players.move1}"

    if move1 == move2:
        return "Game ends in a draw!"
        return f"{list_players.player2} wins by playing {list_players.move2}"
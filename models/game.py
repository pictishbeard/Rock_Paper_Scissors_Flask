from models.player import Player
from models.list_players import *

def winning_player(player1, player2):
    if player1.gesture == "rock" and player2.gesture == "scissors" or player1.gesture == "scissors" and player2.gesture == "paper" or player1.gesture == "paper" and player2.gesture == "rock":
        return f"{player1.name} wins with {player1.gesture}!"

    if player1.gesture == player2.gesture:
        return "draw"
        
    return f"{player2.name} wins with {player2.gesture}!"
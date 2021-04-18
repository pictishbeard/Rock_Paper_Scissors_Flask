from models.player import Player
from models.list_players import *

def winning_player(gesture1, gesture2):
    if gesture1 == "rock" and gesture2 == "scissors":
        return f"{player_1} wins with rock!"
        
    if gesture1 == "scissors" and gesture2 == "paper":
        return f"{player_1} wins with scissors!"
        
    if gesture1 == "paper" and gesture2 == "rock":
        return f"{player_1} wins with paper!"
    
    if gesture1 == gesture2:
        return "draw"
        
    return None
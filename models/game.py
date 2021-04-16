from models.player import *

game1 = Player("Aaron", "Rock", "Not Aaron", "Scissors")
game2 = Player("Joe", "Scissors", "Not Aaron", "Paper")
game3 = Player("Adam", "Paper", "Not Aaron", "Paper")

games = [game1, game2, game3]

def play_game(player1_name, player2_name):
    if player1_choice_move == "Rock" and player2_choice_move == "Scissors":
        return f"{player1_name} wins by playing {player1_choice_move}"
    
    if player1_choice_move == "Scissors" and player2_choice_move == "Paper":
        return f"{player1_name} wins by playing {player1_choice_move}"
    
    if player1_choice_move == "Paper" and player2_choice_move == "Rock":
        return f"{player1_name} wins by playing {player1_choice_move}"

    if player1_choice_move == player2_choice_move:
        return "Game ends in a draw!"

    return f"{player2_name} wins by playing {player2_choice_move}"
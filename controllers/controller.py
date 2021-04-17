from flask import render_template, request
from app import app
from models.list_players import list_players
from models.game import play_game
from models.player import Player


@app.route("/")
def index():
    return render_template('index.html', title="Welcome")

@app.route("/<move1>/<move2>")
def index_results(move1, move2):
    play_game(move1, move2)
    outcome = play_game(move1, move2)
    return render_template('playgame.html', title="Game", winner=play_game(move1, move2))

# @app.route("/<move1>/<move2>")
# def play_game(player1_name, player2_name):
#     return f"{player1_name} wins by playing {move1}"

# @app.route("/rock/paper")
# def rock_paper_loss

# @app.route("/scissors/rock")
# def scissors_rock_loss

# @app.route("/scissors/paper")
# def scissors_paper_win

# @app.route("/paper/rock")
# def paper_rock_win

# @app.route("/paper/scissors")
# def paper_scissors_loss

# @app.route("/paper/paper")
# def paper_draw

# @app.route("/scissors/scissors")
# def scissors_draw

# @app.route("/rock/rock")
# def rock_draw
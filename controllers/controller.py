from flask import render_template, request
from app import app
from models.game import games
from models.player import Player

@app.route("/")
def index():
    return render_template('index.html', title="Welcome", games=games)

@app.route("/", methods=['POST'])
def add_result():
    list_result = Game(player1_name, player1_choice_move, player2_name, player2_choice_move)
    return render_template('index.html', title="Welcome", games=games)

# @app.route("/rock/scissors")
# def rock_scissors_win

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
from flask import render_template, request
from app import app
from models.list_players import list_players
from models.game import *
from models.player import Player


@app.route("/")
def index_homepage():
    return render_template('index.html', title="Welcome")

@app.route("/<gesture1>/<gesture2>")
def game_result(gesture1, gesture2):
    winning_player(gesture1, gesture2)
    result = winning_player(gesture1, gesture2)
    return render_template('playgame.html', title='Play', winner=result)
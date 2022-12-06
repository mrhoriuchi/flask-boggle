from flask import Flask, request, render_template, redirect, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "myboggle123"
app.debug = True

boggle_game = Boggle()


@app.route("/")
def homepage():
    """Makes the board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    number_plays = session.get("number_plays", 0)

    return render_template("index.html", board=board, highscore=highscore, number_plays=number_plays)

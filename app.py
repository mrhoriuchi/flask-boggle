from flask import Flask, request, render_template, redirect, session, jsonify
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


@app.route("/check-word")
def check_word():
    """Checks the word to see if it's valid"""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({"result": response})

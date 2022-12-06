from flask import Flask, request, render_template, redirect, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "myboggle123"
app.debug = True

boggle_game = Boggle()


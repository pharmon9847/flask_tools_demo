from flask import Flask, request, render_template, redirect, flash, jsonify, session
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
import string

app = Flask(__name__)

app.config['SECRET_KEY'] = 'BoyWhatInTheHell1'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = ['Interstellar', 'Rogue One', 'Eternal Sunshine of the Spotless Mind', 'Little Miss Sunshine']

# capitalized_movies = [i.title() for i in MOVIES]

COMPLIMENTS = ["bad ass!", "stellar!", "fucking awesome!",
               "most righteous!", "killer!", "on point!"]

@app.route('/')
def home_page():
    """Shows home page
    """
    session['fav_number'] = 42
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    """Redirects to new home page
    """
    return redirect('/')

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg='You are SO lucky!')


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)


@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/form-2')
def show_form_2():
    return render_template('form-2.html')


@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet-2.html', username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template('hello.html')

@app.route('/movies')
def show_all_movies():
    """show list of all movies in fake db
    """
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=['POST'])
def add_movie():
    # raise
    title = request.form['title']
    # add to pretend DB
    if title in MOVIES:
        flash('That movie already exists in database', 'error')
    else:
        MOVIES.append(title)
        flash('Your movie was added!', 'success')
    return redirect('/movies')
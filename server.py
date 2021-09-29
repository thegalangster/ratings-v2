"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from jinja2 import StrictUndefined

import crud

app = Flask(__name__)
app.secret_key = 'aimee&sarah!'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    movies =  crud.return_all_movies()
    print(movies)
    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movies_detail(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)

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
    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movies_detail(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    users =  crud.return_all_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def users_detail(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)

@app.route('/users', methods=['POST'])
def add_user():
    email = request.form.get('email')
    password = request.form.get('password')
    if crud.get_user_by_email(email):
        flash(f"{email} is taken, please try again")
    else:
        crud.create_user(email, password)
        flash("Account successfully created, now you can login")
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    
    if password == user.password:
        session['id'] = user.user_id
        flash("Logged in!")
    else:
        flash("Authentication failed!")

    return redirect('/')

@app.route('/movies/<movie_id>/rate', methods=['POST'])
def rate_movie(movie_id):
    score = request.form.get('score')
    movie = crud.get_movie_by_id(movie_id)
    user = crud.get_user_by_id(session['id'])
    
    if score.isdigit():
        score_int = int(score)
        if score_int > -1 and score_int < 101:
            crud.create_rating(score, movie, user)
            flash("Created rating!")
        else:
            flash("Rating not within valid range!")
    else:
        flash("Not an integer!")
    return redirect('/')

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)

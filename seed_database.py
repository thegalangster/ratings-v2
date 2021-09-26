"""
os
    This is a module from Python’s standard library. It contains code related to working with your computer’s operating system.

json
    Remember this module from the APIs lab? You’ll need this to load the data in data/movies.json.

choice and randint from random
    choice is a function that takes in a list and returns a random element in the list. randint will return a random number within a certain range. You’ll use both to generate fake users and ratings.

datetime from datetime
    We’ll use datetime.strptime to turn a string into a Python datetime object.

crud, model, and server
    These are all files that you wrote (or will write) — crud.py, model.py, and server.py.
"""
from datetime import datetime
import crud, os, model, server, json, random

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

    movies_in_db = []
    for movie in movie_data:

        title = movie['title']
        overview = movie['overview']
        poster_path = movie['poster_path']

        date_str = movie['release_date']
        format = "%Y-%m-%d"
        release_date = datetime.strptime(date_str, format)

        movie = crud.create_movie(title, overview, release_date, poster_path)
        movies_in_db.append(movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    for n in range(10):
        movie = random.choice(movies_in_db)
        score = random.randint(0, 100)
        crud.create_rating(score, movie, user)



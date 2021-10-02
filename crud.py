"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie( title=title, 
                    overview=overview,
                    release_date=release_date,
                    poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie


#create_movie('The Crow', 'Crows on my front yard', '2022-01-01', 'http://google.com')
def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score=score,
                    movie=movie,
                    user=user)
    db.session.add(rating)
    db.session.commit()

    return rating


#return all movies
def return_all_movies():
    """Query to list all movies"""
    return Movie.query.all()

def get_movie_by_id(id):
    """Query movie by ID"""
    return Movie.query.get(id)

#return all users
def return_all_users():
    """Query to list all users"""
    return User.query.all()

def get_user_by_id(id):
    """Query user by ID"""
    return User.query.get(id)

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
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

# create_rating(100, 1, 1)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
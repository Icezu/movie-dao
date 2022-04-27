from sqlalchemy import Session
from models.movie import Movie

class MovieDao:
    """DAO for movie model."""

    def __init__(self, session:Session):
        self.__session = session

    def get_movies(self):
        """Show all movies."""
        return self.__session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        """Get movie by id."""
        return self.__session.query(Movie).filter_by(movie_id=movie_id).first()

    def add_movie(self, movie: Movie):
        """Add new movie to Movie."""
        self.__session.add(movie)
        self.__session.commit()
        print("Movie added successfully.")
    
    def update_title(self, movie_id, new_title:str ):
        """Update movie name."""
        find_movie = self.__session.query(Movie).filter_by(movie_id=movie_id).first()
        find_movie.title = new_title
        self.__session.commit()
        print("Movie title is updated successfully.")    
    
    def delete_movie(self, movie_id):
        """Delete movie by movie_id"""
        find_movie = self.__session.query(Movie).filter_by(movie_id=movie_id).first()
        self.__session.delete(find_movie)
        print("Movie deleted successfully.")
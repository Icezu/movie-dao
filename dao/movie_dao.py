from sqlalchemy.orm import Session
from models.movie import Movie

class MovieDao:
    """DAO for movie model."""

    def __init__(self, session:Session):
        self.__session = session

    def get_movies(self):
        """Show all movies."""
        return self.__session.query(Movie).all()

    def get_movie_by_id(self, movie_id: int):
        """Get movie by id."""
        return self.__session.query(Movie).filter_by(movie_id=movie_id).first()

    def get_movie_by_title(self, title: str):
        """Get movie by title."""
        return self.__session.query(Movie).filter_by(title=title).first()
    
    def get_movie_by_genre(self, director: str):
        """Get all movie made by director."""
        return self.__session.query(Movie).filter_by(director=director).all()
    
    def get_movie_by_year(self, year: int):
        """Get all movies made in year."""
        return self.__session.query(Movie).filter_by(year=year).all()

    def add_movie(self, movie: Movie):
        """Add new movie to Movie."""
        self.__session.add(movie)
        self.__session.commit()
        print("Movie added successfully.")
    
    def update_title(self, movie_id, new_title:str ):
        """Update movie name by movie_id."""
        find_movie = self.__session.query(Movie).filter_by(movie_id=movie_id).first()
        find_movie.title = new_title
        self.__session.commit()
        print("Movie title is updated successfully.")    
    
    def delete_movie(self, movie_id: int):
        """Delete movie by movie_id"""
        find_movie = self.__session.query(Movie).filter_by(movie_id=movie_id).first()
        self.__session.delete(find_movie)
        self.__session.commit()
        print("Movie deleted successfully.")
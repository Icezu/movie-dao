from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.movie_dao import MovieDao
from dao.user_rating_dao import UserRatingDao

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MovieDatabase(metaclass=Singleton):

    __movie_dao = None
    __user_rating_dao = None

    def __init__(self):
        engine = create_engine("sqlite:///movie_data.db")
        Session = sessionmaker(bind=engine)
        self.__db_session = Session()
    
    def get_movie_dao(self):
        """Get movie dao."""
        if self.__movie_dao is None:
            self.__movie_dao = MovieDao(session=self.__db_session)
        return self.__movie_dao

    def get_user_rating_dao(self):
        """Get user rating dao."""
        if self.__user_rating_dao is None:
            self.__user_rating_dao = UserRatingDao(session=self.__db_session)
        return self.__user_rating_dao
    
    def close(self):
        """Close all database."""
        self.__db_session.close()
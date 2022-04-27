from sqlalchemy import Integer, Column, Text, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True)
    title = Column(Text, (30))
    genre = Column(Text, (30))
    director = Column(Text, (30))
    year = Column(Integer)
    runtime = Column(Integer)

    def __repr__(self):
        return f"Movie(Movie_id={self.movie_id}, title={self.title}, genre={self.genre}, director={self.director}, year={self.year}, runtime={self.runtime})"
    
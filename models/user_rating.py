from sqlalchemy import ForeignKey, Integer, Column, Float
from sqlalchemy.orm import relationship
from .base import Base

class UserRating(Base):
    __tablename__ = "user_rating"
    user_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.movie_id"), nullable=False)
    rating = Column(Float)

    movies = relationship("Movie", back_populates="user_rating")

    def __repr__(self):
        return f"UserRating(user_id={self.user_id}, movie_id={self.movie_id}, rating={self.rating})"
    
from sqlalchemy.orm import Session
from models.user_rating import UserRating

class UserRatingDao:
    """DAO for UserRating model."""

    def __init__(self, session:Session):
        self.__session = session

    def get_rating(self):
        """Show all rating."""
        return self.__session.query(UserRating).all()

    def get_rating_by_id(self, user_id):
        """Get user rating by user id."""
        return self.__session.query(UserRating).filter_by(user_id=user_id).first()

    def add_rating(self, rating: UserRating):
        """Add user rating."""
        self.__session.add(rating)
        self.__session.commit()
        print("Rating added successfully.")
    
    def update_rating(self, user_id, new_rating: float):
        """Update user rating."""
        find_rating = self.__session.query(UserRating).filter_by(user_id=user_id).first()
        find_rating.rating = new_rating
        self.__session.commit()
        print("User rating is updated successfully.")    
    
    def delete_rating(self, user_id):
        """Delete user rating by user_id"""
        find_user_id = self.__session.query(UserRating).filter_by(user_id=user_id).first()
        self.__session.delete(find_user_id)
        print("User rating deleted successfully.")
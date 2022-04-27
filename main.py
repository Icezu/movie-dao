from movie_database import MovieDatabase
from models.movie import Movie
from models.user_rating import UserRating

movie_db = MovieDatabase()

movie_dao = movie_db.get_movie_dao()
user_rating_dao = movie_db.get_user_rating_dao()

# print(movie_dao.get_movies())
# print(movie_dao.get_movie_by_id(1))
# print(movie_dao.get_movie_by_title("Sing"))
# print(movie_dao.get_movie_by_genre("Comedy"))
# print(movie_dao.get_movie_by_year(2016))

# new_movie = Movie(movie_id=51, title="Dune", genre="Action", director="Denis Villeneuve", year=2021, runtime=155)
# movie_dao.add_movie(new_movie)
# print(movie_dao.get_movie_by_title("Dune"))

# movie_dao.update_title(51, "Testing")

# print(movie_dao.get_movie_by_title("Testing"))

# movie_dao.delete_movie(51)

# print(movie_dao.get_movies())

# print(user_rating_dao.get_rating())
# print(user_rating_dao.get_rating_by_id(1001))

# new_user = UserRating(user_id=1051, movie_id=1, rating= 9.1, votes= 1265401)
# user_rating_dao.add_rating(new_user)
# print(user_rating_dao.get_rating_by_id(1051))


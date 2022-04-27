from movie_database import MovieDatabase

movie_db = MovieDatabase()

movie_dao = movie_db.get_movie_dao()
user_rating_dao = movie_db.get_user_rating_dao()

print(movie_dao.get_movies())
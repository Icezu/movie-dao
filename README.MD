# Movie-dao
Movie dao is an application that users can search for movies with details like genre, year, runtime and users can rate movies.

## Movie_data table

1. movie_id - identity value of the movie.
2. title - title of movie.
3. genre - genre of movie.
4. director - director of the movie.
5. year - the year which the movie was created.
6. runtime - length of movie.

## User_rating_data table

1. user_id - identity value of user.
2. movie_id = identity value of the movie.
3. rating - rating value of user.

## Setup

1. Clone this project repository to your machine.

    ``` 
    git clone https://github.com/Icezu/movie-dao.git
    ```

2. Install all required packages.

    ```
    pip install -r requirements.txt
    ```

3. Create your sample database.

    ```
    sqlite3 movie_data.db < movie_database.schema
    or if the above doesn't work
    sqlite3 movie_data.db -init movie_database.schema
    ```

4. Import csv data into the database.

    ```
    sqlite3 movie_data.db
    sqlite3> .import data/movies_data.csv movies
    sqlite3> .import data/user_rating_data.csv user_rating
    sqlite3> .quit
    ```

## Project Documents

[UML Class Diagram](https://github.com/Icezu/movie-dao/wiki/UML-diagram)

[Web API Service](https://github.com/Icezu/movie-dao/wiki/Web-API-Service)
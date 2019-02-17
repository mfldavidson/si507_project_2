from flask import Flask
from movie_tools import Movie
import csv, random

app = Flask(__name__)

# create a route to return the number of movies in the dataset
@app.route('/')
def count_movies():
    return '<h1 style="color:FireBrick;font-family:arial;">{} movies recorded.</h1>'.format(len(movie_instances))

# create a route to return a random list of 10 movies and their IMDB ratings formatted as "<movie> | <IMDB rating>"
@app.route('/movies/ratings/')
def show_ratings():
    random.shuffle(movie_instances)
    movie_rating_string = ''
    for num in range(10):
        movie_rating_string = movie_rating_string + movie_instances[num].getIMDBRatingString() + '<br>'
    return '<h3 style="color:MediumAquaMarine;font-family:arial;">{}</h3>'.format(movie_rating_string)

# if running this file specifically, create a list of instances of Movie using movies_clean.csv, then run the app
if __name__ == '__main__':
    with open("movies_clean.csv", "r") as movies_file:
        movie_lists = []
        moviereader = csv.reader(movies_file)
        next(moviereader)
        for row in moviereader:
            movie_lists.append(row)
        movie_instances = []
        for movie in movie_lists:
            movie_instances.append(Movie(movie))
    app.run()

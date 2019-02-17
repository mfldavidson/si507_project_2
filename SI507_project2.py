from flask import Flask
from movie_tools import Movie
import csv

app = Flask(__name__)

@app.route('/')
def count_movies():
    with open("movies_clean.csv", "r") as movies_file:
        movie_lists = []
        moviereader = csv.reader(movies_file)
        next(moviereader)
        for row in moviereader:
            movie_lists.append(row)
    return '<h1>{} movies recorded.</h1>'.format(len(movie_lists))

if __name__ == '__main__':
    app.run()

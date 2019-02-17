# SI 507 Project 2: Movies App and ER Diagram
## About the Movies App
This program in SI507_project_2.py is a Flask app that uses the Movie class defined in movie_tools.py (by importing movie_tools.py into SI507_project_2.py) to create routes that use the dataset movies_clean.csv. Before running the program, the app opens the movies_clean CSV file, reads it into a list of lists, and then creates a list of instances of the Movie class to use in the app.

### About movie_tools.py
movie_tools.py defines the class Movie, which takes an input of a list of data about one movie from movies_clean.csv. It has instance variables that map to the fields provided in movies_clean.csv, with the string "NA" if no data is available. In addition to the init method, Movie has str and repr methods that return a string representing the value of self.title, the title of the movie. Movie also has the method self.getIMDBRatingString which returns a string in format `<self.title> | <self.imdb_rating>`. For example, "Lord of the Rings: the Fellowship of the Ring | 8.8".

### The routes available in the banking app include:
- The home route (/) displays in red h1 text the number of movies recorded in the app by counting the length of the list of instances of Movie.
- The route `movies/ratings/` displays a random list of 10 movies and their IMDB ratings on individual lines, using the self.getIMDBRatingString method.

# How to Run the Program
This program was written with Python Anaconda and the Flask module using a virtual environment. Requirements to run the program can be found in requirements.txt. To install everything from requirements.txt, download the requirements.txt file, activate your virtual environment, and then enter the following in your shell: `pip install -r requirements.txt`.

In order to run the program, make sure you are in the same directory as all the files, and then enter the following in your shell: `python SI507_project_2.py runserver`. The program can then be found running at `localhost:5000` plus the correct route in your browser.

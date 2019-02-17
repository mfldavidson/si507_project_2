# That class should have any instance variables and/or method(s) you think will be useful for building your Flask app, and at least one of your Flask app's routes should create instances of that class.
#
# We suggest that you make this plan based on your goals for the Flask app (detailed below), and go back and forth between the two Python files making plans as you write code (similarly to how you might have gone back and forth between your lab3_code.py and your SI507_project1.py code to work on Project 1!). We expect you to use instances of this class in the Flask app.
#
# It is also possible that you will choose to define additional function/s in movies_tools.py and invoke them in the Flask code, but it is not necessary to do so. You can make your own design decisions here.
#
# We also suggest that, as you work, you have, beneath an if __name__ == "__main__": statement, code that opens up the clean movies data file and uses its contents to test out some instances of this class -- in order to ensure it works as you want it to. It's more annoying to debug inside Flask than it is to debug code outside Flask first, so read what your goals are, make sure your class works, and THEN integrate it into the app!

class Movie():
    def __init__(self, movie_info_list):
        self.title = movie_info_list[0]
        self.us_gross = movie_info_list[1]
        self.worldwide_gross = movie_info_list[2]
        self.us_dvd_sales = movie_info_list[3]
        self.production_budget = movie_info_list[4]
        self.release_date = movie_info_list[5]
        self.mpaa_rating = movie_info_list[6]
        self.run_time_min = movie_info_list[7]
        self.distributor = movie_info_list[8]
        self.source = movie_info_list[9]
        self.major_genre = movie_info_list[10]
        self.creative_type movie_info_list[11]
        self.director = movie_info_list[12]
        self.rotten_tomatoes_rating = movie_info_list[13]
        self.imdb_rating = movie_info_list[14]
        self.imdb_votes = movie_info_list[15]


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
        self.creative_type = movie_info_list[11]
        self.director = movie_info_list[12]
        self.rotten_tomatoes_rating = movie_info_list[13]
        self.imdb_rating = movie_info_list[14]
        self.imdb_votes = movie_info_list[15]

    def __str__(self):
        return '{}'.format(self.title)

    def __repr__(self):
        return '{}'.format(self.title)

    def getIMDBRatingString(self):
        return '{} | {}'.format(self.title, self.imdb_rating)

import webbrowser


# create class Movie
class Movie():
        # function to create movie objects
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_year, movie_director, movie_stars):  # NOQA
                # initializes instance variables with arguments
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.release_year = movie_release_year
                self.director = movie_director
                self.stars = movie_stars

        # function to link to trailer on Youtube
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)

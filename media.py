import webbrowser

class Video():
    """ This class information about video"""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Title - " + self.title)
        print("Duration in minutes - " + str(self.duration))


class Movie(Video):
    """ This class information about movies"""
    def __init__(self, title, duration, storyline,
                 poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        Video.show_info(self)
        print("Storyline - " + self.storyline)
        print("URL Poster - " + self.poster_image_url)
        print("URL Trailer - " + self.trailer_youtube_url)
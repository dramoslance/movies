import webbrowser


class Movie:       
    """This class represents movies entity, created to storage all information
    related."""
    
    def __init__(self):
        """ Inits the movie instance."""
        self.data = []
        self.visits = 0        
        
    def set_title(self, title):
        """Sets the title for a movie.

        Args:
            title: A string with movie title.

        Raise:
            None.
        """
        self.title = title

    def set_price(self, price):
        """Sets the price for a movie.

        Args:
            price: A float with movie price.

        Raise:
            None.
        """
        self.price = price
    
    def set_story_line(self, story_line):
        """Sets the story line for a movie.

        Args:
            story_line: A string with movie story line.
            
        Raise:
            None.
        """
        self.story_line = story_line

    def set_poster_image(self, poster_image_url):
        """Sets the poster image url for a movie.

        Args:
            poster_image_url: A string with movie poster image url.

        Raise:
            None.
        """
        self.poster_image_url = poster_image_url
    
    def set_url_trailer(self, trailer_youtube_url):
        """Sets the trailer youtube url for a movie.

        Args:
            trailer_youtube_url: A string with movie trailer youtube url.

        Raise:
            None.
        """
        self.trailer_youtube_url = trailer_youtube_url

    def set_synopsis_url(self, synopsis_url):
        """Set url to fully shows the content of movie.

        Args:
            synopsis_url: A string with movie information url.

        Raise:
            None.
        """
        self.synopsis_url = synopsis_url

    def set_publishment_date(self, publishment_date):
        """Sets the publishment date for a movie.

        Args:
            date_publish: A float with movie publishment date.

        Raise:
            None.
        """
        self.publishment_date = publishment_date

    def set_visits(self, visits):
        """Sets the visits for a movie.

        Args:
            visits: A integer with movie visits.

        Raise:
            None.
        """
        self.visits = visits

    def set_actor(self, actor):
        """ Allows to set actor to the movie"""
        self.actor = actor;

    def show_trailer(self):
        """Shows movie trailer in browser.

        Use the corresponding youtube url to show movie trailer by
        using webbrowser

        Args:
            None.
            
        Raise:
            None.
        """
        self.visits = self.visits + 1;
        webbrowser.open(self.trailer_youtube_url);
    


class Actor():
    """Represents actors of the movies"""

    def __init__(self):
        self.data = []

    def __init__(self, name, gender, nationality, age):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.age = age

    def set_name(self, name):
        """Sets the name for an actor.

        Args:
            name: A string with actor name.

        Raise:
            None.
        """
        self.name = name

    def set_gender(self, gender):
        """Sets the gender for an actor.

        Args:
            gender: A string with actor gender.

        Raise:
            None.
        """
        self.gender = gender

    def set_nationality(self, nationality):
        """Sets the nationality for an actor.

        Args:
            nationality: A string with actor nationality.

        Raise:
            None.
        """
        self.nationality = nationality

    def set_age(self, age):
        """Sets the age for an actor.

        Args:
            age: A string with actor age.

        Raise:
            None.
        """
        self.age = age
        
import webbrowser


class Movie(object):
    """This class represents movies entity, created to storage all information
    related."""

    def __init__(self):
        """ Inits the movie instance."""
        self.data = []
        self._visits = 0

    @property
    def title(self):
        """Gets the title for a movie.

        Args:
            self: current instance.

        Returns:
            Movie title.

        Raise:
            None.
        """
        return self._title

    @title.setter
    def title(self, value):
        """Sets the title for a movie.

        Args:
            value: A string with movie title.

        Raise:
            None.
        """
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    @property
    def price(self):
        """Gets the price for a movie.

        Args:
            self: current instance.

        Returns:
            Movie price.

        Raise:
            None.
        """
        return self._price

    @price.setter
    def price(self, value):
        """Sets the price for a movie.

        Args:
            value: A float with movie price.

        Raise:
            None.
        """
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def story_line(self):
        """Gets the story line for a movie.

        Args:
            self: current instance.

        Returns:
            Movie story line.

        Raise:
            None.
        """
        return self._story_line

    @story_line.setter
    def story_line(self, value):
        """Sets the story line for a movie.

        Args:
            value: A string with movie story line.

        Raise:
            None.
        """
        self._story_line = value

    @story_line.deleter
    def story_line(self):
        del self._story_line

    @property
    def poster_image_url(self):
        """Gets the poster image url for a movie.

        Args:
            self: current instance.

        Returns:
            Movie poster image url.

        Raise:
            None.
        """
        return self._poster_image_url

    @poster_image_url.setter
    def poster_image_url(self, value):
        """Sets the poster image url for a movie.

        Args:
            value: A string with movie poster image url.

        Raise:
            None.
        """
        self._poster_image_url = value

    @poster_image_url.deleter
    def poster_image_url(self):
        del self._poster_image_url

    @property
    def trailer_youtube_url(self):
        """Gets the trailer youtube url for a movie.

        Args:
            self: current instance.

        Returns:
            Movie trailer youtube url.

        Raise:
            None.
        """
        return self._trailer_youtube_url

    @trailer_youtube_url.setter
    def trailer_youtube_url(self, value):
        """Sets the trailer youtube url for a movie.

        Args:
            value: A string with movie trailer youtube url.

        Raise:
            None.
        """
        self._trailer_youtube_url = value

    @trailer_youtube_url.deleter
    def trailer_youtube_url(self):
        del self._trailer_youtube_url

    @property
    def synopsis_url(self):
        """Gets the synopsis url for a movie.

        Args:
            self: current instance.

        Returns:
            Movie synopsis url.

        Raise:
            None.
        """
        return self._synopsis_url

    @synopsis_url.setter
    def synopsis_url(self, value):
        """Set url to fully shows the content of movie.

        Args:
            value: A string with movie information url.

        Raise:
            None.
        """
        self._synopsis_url = value

    @synopsis_url.deleter
    def synopsis_url(self):
        del self._synopsis_url

    @property
    def publishment_date(self):
        """Gets the publishment date for a movie.

        Args:
            self: current instance.

        Returns:
            Movie publishment date.

        Raise:
            None.
        """
        return self._publishment_date

    @publishment_date.setter
    def publishment_date(self, value):
        """Sets the publishment date for a movie.

        Args:
            value: A float with movie publishment date.

        Raise:
            None.
        """
        self._publishment_date = value

    @publishment_date.deleter
    def publishment_date(self):
        del self._publishment_date

    @property
    def visits(self):
        """Gets the visits for a movie.

        Args:
            self: current instance.

        Returns:
            Movie visits.

        Raise:
            None.
        """
        return self._visits

    @visits.setter
    def visits(self, value):
        """Sets the visits for a movie.

        Args:
            value: A integer with movie visits.

        Raise:
            None.
        """
        self._visits = value

    @visits.deleter
    def visits(self):
        del self._visits

    @property
    def actor(self):
        """Gets the actor for a movie.

        Args:
            self: current instance.

        Returns:
            Movie actor.

        Raise:
            None.
        """
        return self._actor

    @actor.setter
    def actor(self, value):
        """ Allows to set actor to the movie

        Args:
            value: actor instance

        Returns:
            None.

        Raises:
            None.
        """
        self._actor = value

    @actor.deleter
    def actor(self):
        del self._actor

    def show_trailer(self):
        """Shows movie trailer in browser.

        Use the corresponding youtube url to show movie trailer by
        using webbrowser

        Args:
            None.

        Raise:
            None.
        """
        self.visits = self.visits + 1
        webbrowser.open(self.trailer_youtube_url)


class Actor(object):
    """Represents actors of the movies"""

    def __init__(self):
        self.data = []

    def __init__(self, name, gender, nationality, age):
        self._name = name
        self._gender = gender
        self._nationality = nationality
        self._age = age

    @property
    def name(self):
        """Gets the actor name.

        Args:
            self: current instance.

        Returns:
            Actor name.

        Raise:
            None.
        """
        return self._name

    @name.setter
    def name(self, value):
        """Sets the name for an actor.

        Args:
            value: A string with actor name.

        Raise:
            None.
        """
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def gender(self):
        """Gets the actor gender.

        Args:
            self: current instance.

        Returns:
            Actor gender.

        Raise:
            None.
        """
        return self._gender

    @gender.setter
    def gender(self, value):
        """Sets the gender for an actor.

        Args:
            value: A string with actor gender.

        Raise:
            None.
        """
        self._gender = value

    @gender.deleter
    def gender(self):
        del self._gender

    @property
    def nationality(self):
        """Gets the actor nationality.

        Args:
            self: current instance.

        Returns:
            Actor nationality.

        Raise:
            None.
        """
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        """Sets the nationality for an actor.

        Args:
            value: A string with actor nationality.

        Raise:
            None.
        """
        self._nationality = value

    @nationality.deleter
    def nationality(self):
        del self._nationality

    @property
    def age(self):
        """Gets the actor age.

        Args:
            self: current instance.

        Returns:
            Actor age.

        Raise:
            None.
        """
        return self._age

    @age.setter
    def age(self, value):
        """Sets the age for an actor.

        Args:
            value: A string with actor age.

        Raise:
            None.
        """
        self._age = value

    @age.deleter
    def age(self):
        del self._age

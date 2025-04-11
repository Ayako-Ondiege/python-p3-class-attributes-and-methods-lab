class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre 

        #Step 1: Increment count using class method
        Song.add_song_to_count()


        #Step 2: Add genre and artist to their respective lists
        Song.genres.append(genre)
        Song.artists.append(artist)
        
        #Step 3: Update all relevant class-level stats using class methods

        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

        Song.add_to_genres()
        Song.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))
        #Keep only unique genres
            
    @classmethod
    def add_to_artists(cls):
        #keep only unique artists
        cls.artists = list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[cls.genres[-1]] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[cls.artists[-1]] = 1



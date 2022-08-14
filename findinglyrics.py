
#!/usr/bin/python3
import lyricsgenius as lg

class song_lyrics:
    def __init__(self, lg_song, lg_artist):
        self.api_key =  'xvx4-YJzMnTVn4uPWt_kU6oRE2IiLZnSYqgKZO7g8iQIRkagmePnp8awHaKWLETM'
        self.lg_song = lg_song
        self.lg_artist = lg_artist

    def find_lyris(self):
        genius_obj = lg.Genius(self.api_key)
        lyrics = genius_obj.search_song(self.lg_song, self.lg_artist)
        print(lyrics.lyrics)

if __name__ == '__main__':
    song = 'love more'
    artist = 'chris brown'
    class_obj = song_lyrics(song, artist)
    class_obj.find_lyris()

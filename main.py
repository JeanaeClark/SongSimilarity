import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup
import requests

cid = '0cad5195dfd04884b84ba221fe400bff'
secret = '212724fad9f6414fb40a0d2caf57f4ee'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def scrape_lyrics(artistname, songname):
    # https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3
    symbolString = "\"`~!@#$%^&*()_+-=[{]}\|;:',<.>/?"
    artistname2 = str(artistname.replace(' ','-')).lower() if ' ' in artistname else str(artistname).lower()
    songname2 = str(songname.replace(' ','-')).lower() if ' ' in songname else str(songname).lower()
    songname2 = songname2.translate({ord(i): "-" for i in symbolString})
    page = requests.get('https://www.songlyrics.com/'+ artistname2 + '/' + songname2 + '-lyrics/')
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find("p", id="songLyricsDiv")
    return lyrics.get_text()

songs = ["First", "Second"]
for i in songs:
    print("{} Song: \n".format(i))
    song = input("\tEnter song title: \n\t")

    r = sp.search(song, type = "track", limit=1, offset=0, market=None)

    print("\t{} by {}".format(r["tracks"]["items"][0]["name"],r["tracks"]["items"][0]["artists"][0]["name"]))
    print("\tSong Sample (if available): {}".format(r["tracks"]["items"][0]["preview_url"]))
    response = input("\tIs this the correct song? Y or N\n\t")
    if response == "Y":
        if i == "First":
            firstSong = r["tracks"]["items"][0]["id"]
        if i == "Second":
            secondSong = r["tracks"]["items"][0]["id"]
    elif response == "N":
        artist = input("\tEnter song artist: \n\t")
        q = "{} {}".format(song,artist)
        r = sp.search(q, type = "track", limit=1, offset=0, market=None)
        print("\t{} by {}".format(r["tracks"]["items"][0]["name"],r["tracks"]["items"][0]["artists"][0]["name"]))
        print("\tSong Sample (if available): {}".format(r["tracks"]["items"][0]["preview_url"]))
        response = input("\tIs this the correct song? Y or N\n\t")
        if response == "Y":
            if i == "First":
                firstSong = r["tracks"]["items"][0]["id"]
            if i == "Second":
                secondSong = r["tracks"]["items"][0]["id"]
        else:
            print("Error")
            break
    print("\n\n")


firstSongTitle = sp.track(firstSong)["name"]
firstSongArtist = sp.track(firstSong)["artists"][0]["name"]
firstSongLyrics = scrape_lyrics(firstSongArtist, firstSongTitle)


secondSongTitle = sp.track(secondSong)["name"]
secondSongArtist = sp.track(secondSong)["artists"][0]["name"]
secondSongLyrics = scrape_lyrics(secondSongArtist, secondSongTitle)

print(firstSongLyrics)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '0cad5195dfd04884b84ba221fe400bff'
secret = '212724fad9f6414fb40a0d2caf57f4ee'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

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
    else:
        artist = input("\tEnter song artist: \n\t")
        q = "{} {}".format(song,artist)
        print(q)
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

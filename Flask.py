from flask import Flask, render_template, request
import json
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
global liste_10

app = Flask(__name__)
with open("genres.json") as js:
    genres = json.load(js)


def top_10(sanatcı):
    liste_10= list()
    SPOTIPY_CLIENT_ID="39e05027a86c4cfc9a843b285ec2afff"
    SPOTIPY_CLIENT_SECRET="d3e7253623b24f5d996462cfc80aae33"
    SPOTIPY_REDIRECT_URI="http://127.0.0.1:5000/"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
    search = sp.search(sanatcı,limit=1, offset=0, type="artist", market=None)
    artist_ıd = search["artists"]["items"][0]['external_urls']["spotify"][32:]

    results = sp.artist_top_tracks(artist_ıd,country="TR")
    for i in range(len(results["tracks"])):
        dict = {}
        dict["artist"] = results["tracks"][i]["album"]["artists"][0]["name"]
        dict["song_name"] = results["tracks"][i]["name"]
        dict["album_image_url"] = results["tracks"][i]["album"]["images"][0]["url"]
        dict["prewiev_url"] = results["tracks"][i]["preview_url"]
        liste_10.append(dict)

    return liste_10

@app.route("/tracks/rock")
def rock():
    sec_sanatcı = random.choice(genres["rock"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))

@app.route("/tracks/alternative rock")
def alternative_rock():
    sec_sanatcı = random.choice(genres["alternative rock"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/pop")
def pop():
    sec_sanatcı = random.choice(genres["pop"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/blues")
def blues():
    sec_sanatcı = random.choice(genres["blues"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/country")
def country():
    sec_sanatcı = random.choice(genres["country"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/electronic")
def electronic():
    sec_sanatcı = random.choice(genres["electronic"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/jazz")
def jazz():
    sec_sanatcı = random.choice(genres["jazz"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/r&b")
def rb():
    sec_sanatcı = random.choice(genres["r&b"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))


@app.route("/tracks/rap")
def rap():
    sec_sanatcı = random.choice(genres["rap"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))

@app.route("/tracks/reggae")
def reggae():
    sec_sanatcı = random.choice(genres["reggae"])
    return render_template("genre.html", variable=top_10(sec_sanatcı))

@app.route('/tracks', methods=['GET', 'POST'])
def server():
    return render_template('index.html')



if __name__ =="__main__":

    app.run(debug=True)
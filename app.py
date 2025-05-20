from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        res = requests.get("https://api.jikan.moe/v4/top/anime?type=movie")
        anime_list = res.json().get("data", [])
    except:
        anime_list = []
    return render_template("index.html", anime_list=anime_list)

@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            try:
                res = requests.get("https://api.jikan.moe/v4/anime", params={"q": query})
                results = res.json().get("data", [])
            except:
                results = []
    return render_template("search.html", results=results)

@app.route("/anime/<int:anime_id>")
def anime_detail(anime_id):
    try:
        res = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}")
        anime = res.json().get("data", {})
    except:
        anime = {}
    return render_template("anime_detail.html", anime=anime)
if __name__ == "__main__":
    app.run(debug=True)
    
""" from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.jikan.moe/v4/top/anime?type=movie")
    data = response.json()
    anime_data = data['data']

    anime_list = []

    for anime in anime_data:
        anime_list.append({
            'title': anime['title'],
            'id': anime['mal_id'],
            'image_url': anime['images']['jpg']['image_url']
        })

    return render_template("index.html", animes=anime_list)

@app.route("/anime/<int:id>")
def anime_detail(id):
    response = requests.get(f"https://api.jikan.moe/v4/anime/{id}")
    data = response.json()
    anime = data['data']

    details = {
        'id': anime['mal_id'],
        'title': anime['title'],
        'image_url': anime['images']['jpg']['large_image_url'],
        'synopsis': anime.get('synopsis'),
        'score': anime.get('score'),
        'rank': anime.get('rank'),
        'trailer_url': anime['trailer']['url'] if anime['trailer'] and anime['trailer']['url'] else None
    }

    return render_template("anime.html", anime=details) 
if __name__ == "__main__":
    app.run(debug=True) """
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.jikan.moe/v4/top/anime?type=movie")
    data = response.json()
    anime_list = data.get('data', [])
    
    animes = []
    for anime in anime_list:
        animes.append({
            'id': anime['mal_id'],
            'title': anime['title'],
            'image_url': anime['images']['jpg']['image_url'],
            'score': anime.get('score'),
            'year': anime.get('year'),
        })
    
    return render_template("index.html", animes=animes)

@app.route("/anime/<int:id>")
def anime_detail(id):
    response = requests.get(f"https://api.jikan.moe/v4/anime/{id}")
    data = response.json().get('data', {})
    
    anime = {
        'title': data.get('title'),
        'image_url': data.get('images', {}).get('jpg', {}).get('image_url'),
        'synopsis': data.get('synopsis'),
        'score': data.get('score'),
        'year': data.get('year'),
        'genres': [genre['name'] for genre in data.get('genres', [])],
        'duration': data.get('duration'),
        'rating': data.get('rating')
    }
    
    return render_template("anime.html", anime=anime)

if __name__ == "__main__":
    app.run(debug=True)

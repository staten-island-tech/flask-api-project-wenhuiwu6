from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.jikan.moe/v4/top/anime?type=movie")
    data = response.json()
    anime_data = data['data']

    anime_datas = []

    for anime in anime_data:
        anime_datas.append({
            'title': anime['title'],
            'image_url': anime['images']['jpg']['image_url'],
            'score': anime.get('score', 'N/A'),
            'url': anime['url']
        })
    return render_template("index.html", animes=anime_datas)

if __name__ == '__main__':
    app.run(debug=True)

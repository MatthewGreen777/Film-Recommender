import requests
from flask import Flask, jsonify, request, send_from_directory
import random

app = Flask(__name__, static_folder='front-end')

HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDE1YWRiZjAzM2JiZTBmZjVkM2E4YTk5M2Y3NTgwNSIsIm5iZiI6MTcyODA3MDM2NC4xNjE3NjIsInN1YiI6IjY3MDA0MGU4YzlhMTBkNDZlYTdjZTI2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ALw111-0iTaOBTnDpnOlAWVpX7KeXeYot0hfrX3lY_E"
}

GENRES = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]

# Serve static files for the front-end
@app.route('/')
@app.route('/<path:path>')
def serve_static_files(path='index.html'):
    return send_from_directory(app.static_folder, path)

#include_adult=true Option to include adult content

# Route /genre-search?genre={int}
@app.route("/genre-search", methods=["GET"])
def genre_search():
    genre = request.args.get('genre')
    page = request.args.get('currentPage', 1)
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&sort_by=popularity.desc&with_genres={genre}&page={page}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

# Route /title-search?title={str}
@app.route("/title-search", methods=["GET"])
def title_search():
    title = request.args.get('title')
    url = f"https://api.themoviedb.org/3/search/movie?include_adult=false&original_language=en&query={title}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

# Route /random
@app.route("/random", methods=["GET"])
def randomMovie():
    randomIndex = random.randint(0, len(GENRES)-1)
    randomID = GENRES[randomIndex]
    randomYear = random.randint(1940, 2024)
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&with_original_language=en&sort_by=popularity.desc&with_genres={randomID}&primary_release_year={randomYear}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

# Run the app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

#Needed functions for the backend
#https://developer.themoviedb.org/reference/intro/getting-started
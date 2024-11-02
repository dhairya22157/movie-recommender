# app.py
from flask import Flask, render_template, request, jsonify
import pickle
import requests

app = Flask(__name__)

# Load the model data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d7e63b12aa8f6a2207af26f855ecd503&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

@app.route('/')
def index():
    movie_list = movies['title'].values
    return render_template('index.html', movie_list=movie_list)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie = request.form['movie']
    recommended_movie_names, recommended_movie_posters = recommend(movie)
    recommendations = [
        {"title": name, "poster": poster}
        for name, poster in zip(recommended_movie_names, recommended_movie_posters)
    ]
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

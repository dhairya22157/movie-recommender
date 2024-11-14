Movie Recommender System 🎥
A machine learning-based movie recommender system that suggests similar movies based on user input. Built with Flask for the web interface and deployed on [Render](https://render.com), accessible [here](https://movie-recommender-8aae.onrender.com).

About
This project is a movie recommendation system that uses machine learning to suggest movies based on similarities in genres, cast, and other features. The system relies on a collaborative filtering approach, using a dataset of 5,000 movies from Kaggle.

gitFeatures
- Movie Recommendations: Suggests similar movies based on input titles.
- Simple Web Interface: Built with Flask for ease of use.
- Fast Predictions: Utilizes a pre-trained model saved as a `.pkl` file for quick recommendations.

Tech Stack
- Backend: Python, Flask
- Machine Learning Libraries: Scikit-Learn, Pandas, Numpy
- Frontend (optional): HTML, CSS
- Deployment Platform: Render

Data Source
The recommender system uses two datasets sourced from Kaggle:
1. tmdb_5000_movies.csv - Contains metadata for movies, including genres and keywords.
2. tmdb_5000_credits.csv - Provides cast and crew information.

These datasets are used to capture a variety of features for more accurate recommendations.

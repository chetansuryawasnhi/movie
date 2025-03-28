# Movie Recommendation System

vusit = https://m-rs-chetan.streamlit.app/

Overview

This project is a Movie Recommendation System that suggests movies to users based on content similarity. The system uses Content-Based Filtering with a Bag of Words (BoW) approach to analyze movie descriptions and recommend similar movies. The model is deployed using Streamlit for a user-friendly interface.

Features

Content-Based Filtering: Recommends movies based on their descriptions and metadata.

Bag of Words (BoW) Approach: Vectorizes text data to find similar movies.

Streamlit Deployment: Provides an interactive web-based interface.

Efficient Movie Suggestions: Finds similar movies based on user-selected input.

Technologies Used

Python: Core programming language.

Pandas: For data manipulation and preprocessing.

Scikit-learn: Used for text vectorization (CountVectorizer) and similarity computation (cosine similarity).

Streamlit: For deploying the application.

Installation

Clone the repository:

git clone https://github.com/your-repo/movie-recommendation-system.git
cd movie-recommendation-system

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

How It Works

The dataset is preprocessed and converted into a Bag of Words (BoW) representation.

Cosine similarity is used to measure similarity between movies.

Users select a movie, and the system recommends similar movies based on their descriptions.

The application is served using Streamlit, providing a simple and intuitive UI.

Usage

Open the web interface.

Select a movie from the dropdown.

View recommended movies based on content similarity.

Future Enhancements

Improve recommendations using TF-IDF instead of BoW.

Integrate user ratings and collaborative filtering.

Deploy as a web application using Flask/FastAPI.

Contributors

Chetan Suryawanshi (Developer)

License

This project is licensed under the MIT License.


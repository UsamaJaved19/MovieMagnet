# Movie Recommendation System

### Overview
The **Movie Recommendation System** is a content-based recommendation engine that suggests movies to users based on their preferences. This system analyzes movie metadata, specifically **tags**, and recommends movies similar to those the user has liked or rated highly. The recommendation engine uses **Cosine Similarity** to measure the similarity between movies based on their tags, extracted using **CountVectorizer**. The system provides a user-friendly interface built using **Streamlit**.

The system is built using the **TMDb 5000 Movies** dataset, which contains extensive metadata about a wide range of movies, including genres, cast, directors, and plot summaries, as well as relevant tags for each movie.

### Features
- **Cosine Similarity Algorithm**: Measures the similarity between movies by calculating the cosine of the angle between two movie feature vectors based on their tags.
- **Movie Similarity**: Recommends movies based on content similarity (analyzing tags, genres, cast, etc.).
- **User Preferences**: Customizes suggestions based on user input or previously liked/rated movies.
- **Search Functionality**: Allows users to search for a specific movie and receive recommendations.
- **Content-Based Filtering**: Uses metadata tags (such as genre, director, cast, and keywords) to recommend similar movies.
- **Streamlit Web Interface**: An easy-to-use, interactive web app to engage with the recommendation system.

### Dataset
- **Dataset Name**: TMDb 5000 Movies
- **Source**: The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and contains metadata such as:
  - Movie Title
  - Genres
  - Overview (description)
  - Cast and Crew information
  - Keywords/Tags
  - Popularity and Ratings

### Technologies Used
- **Python**: The main programming language used for building the recommendation engine.
- **Pandas**: For data manipulation and cleaning.
- **Scikit-Learn**: For implementing machine learning algorithms, including **Cosine Similarity** and **CountVectorizer**.
- **CountVectorizer**: For extracting features from the movie tags.
- **Cosine Similarity**: For measuring the similarity between movies based on their feature vectors (tags).
- **Streamlit**: For building the interactive web app interface.
  
### Installation
To get started with the Movie Recommendation System, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Movie-Recommendation-System.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Movie-Recommendation-System
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Download the **TMDb 5000 Movies** dataset from Kaggle and place the dataset files (e.g., `tmdb_5000_movies.csv`) into the project directory.

### Usage
1. Ensure the dataset (TMDb 5000 Movies) is properly placed in the project directory.
2. To run the Streamlit app locally, use the following command:
   ```bash
   streamlit run app.py
   ```
3. This will launch the Movie Recommendation System in your default web browser. You can input a movie name, and the system will provide recommendations based on content similarity using **Cosine Similarity** on the extracted tags from the dataset.

### Example Output
- **Recommendations**: When the user searches for a movie (e.g., "Inception"), the system might recommend other movies such as "Interstellar," "The Prestige," or "Memento," based on cosine similarity calculated from the movie tags.
- **Similarity Score**: A list of movies with their similarity scores to the input movie will be displayed.

### Data Source
- **Dataset**: [TMDb 5000 Movies](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Description**: This dataset contains metadata for over 5000 movies, including title, genres, plot summaries, cast/crew information, and tags for each movie.

### Future Improvements
- **Hybrid Filtering**: Incorporating both content-based filtering and collaborative filtering for enhanced recommendations.
- **User Profile Tracking**: Allowing users to create profiles that store their preferences and adjust recommendations over time.
- **Rating System**: Integrating a rating system for users to rate movies, improving the accuracy of recommendations.

### Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and create a pull request with detailed information about the changes.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contact Information
For further inquiries or suggestions, feel free to reach out at:
- **Email**: usama11javed@outlook.com


## Recipe Recommendation App
This project aims to provide users with personalized recipe recommendations based on the ingredients they have. The app utilizes web scraping techniques to gather Cooking Mama recipes, implements a recommendation system using cosine similarity, and presents the recommendations through a Flask web application.


![ezgif-7-1e1b2ac6a4](https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/37ab3d11-fc0e-4a8e-8c96-fe527e88170a)


<img width="870" alt="image" src="https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/53b1658e-ca7d-4ee6-8221-87c01b985a27">

<img width="907" alt="image" src="https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/15b69771-e7af-4b51-929d-6c798704ebee">

## Purpose
The purpose of this project is to offer users an easy and convenient way to discover new recipes based on the ingredients they already have at home. By leveraging Cooking Mama recipes and advanced recommendation algorithms, users can explore a variety of cooking options tailored to their preferences and available ingredients.

## Key Features

- **Web Scraping:** The project scrapes Cooking Mama recipes from a wiki page to build a dataset of food items along with their ingredients and image URLs.

- **Recommendation System:** A recommendation system based on cosine similarity calculates the similarity between user-provided ingredients and recipe ingredients. This allows the app to suggest recipes that best match the user's input.

- **Flask Web Application:** The core functionality is wrapped into a user-friendly web application using Flask, allowing users to input their ingredients and receive recipe recommendations in real-time.

## Technologies Used

- **Python:** The primary programming language used for web scraping, data processing, and backend development.

- **Flask:** A lightweight web framework for building the web application and handling user requests.

- **Beautiful Soup:** A Python library for pulling data out of HTML and XML files, essential for web scraping.

- **SciKit Learn, Cosine Similarity:** A mathematical technique used to measure the similarity between two non-zero vectors, employed in the recommendation system to compare ingredient lists.

- **HTML/CSS/JavaScript:** Frontend technologies utilized for designing the user interface and enhancing the user experience.

## Usage
Users can access the Recipe Recommendation App through their web browser. Upon visiting the site, they can input a list of ingredients they have on hand. The app then processes the input, calculates recipe recommendations based on similarity, and displays them along with relevant information such as recipe names, images, and ingredient matches.

## Future Enhancements
- **User Authentication:** Implement user accounts to save favorite recipes and personalize recommendations. If a recipe is chosen, gather real recipe ingredient/cooking process data.
- **Improved Recommendation Algorithm:**: Explore more advanced recommendation algorithms to enhance the accuracy and relevance of recipe suggestions.
- **Enhanced UI/UX:** Continuously improve the user interface and experience to make recipe exploration more intuitive and enjoyable.

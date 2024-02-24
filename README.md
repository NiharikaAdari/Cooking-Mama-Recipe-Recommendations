## Recipe Recommendation App
This project aims to provide users with personalized recipe recommendations based on the ingredients they have. The app utilizes web scraping techniques to gather Cooking Mama recipes, implements a recommendation system using cosine similarity, and presents the recommendations through a Flask web application.


![demo](https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/7b3fa27f-5139-477a-a7f7-30ffe065ba1a)



## Purpose
The purpose of this project is to offer users an easy and convenient way to discover new recipes based on the ingredients they already have at home. By leveraging Cooking Mama recipes and advanced recommendation algorithms, users can explore a variety of cooking options tailored to their preferences and available ingredients.

<img width="1233" alt="image" src="https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/9ac4e807-dbf7-43f5-86df-79f92de9e016">


Hover over a recipe card to see the ingredients!
<img width="592" alt="image" src="https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/760fe825-9bae-448d-a82a-86a6a7c5f5f1">

Click a recipe card to get the recipe!
<img width="591" alt="image" src="https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/0a1e37b3-febd-43bc-8cff-65889b39ed37">

## Key Features

- **Web Scraping:** The project scrapes Cooking Mama recipes from a wiki page to build a dataset of food items along with their ingredients and image URLs. https://cookingmama.fandom.com/wiki/Foods

- **Recommendation System:** A recommendation system based on cosine similarity calculates the similarity between user-provided ingredients and recipe ingredients. This allows the app to suggest recipes that best match the user's input.

- **Flask Web Application:** The core functionality is wrapped into a user-friendly web application using Flask, allowing users to input their ingredients and receive recipe recommendations in real-time. Users can effortlessly input their available ingredients and receive personalized recipe suggestions instantly. The application boasts intuitive features such as a carousel scroll system for recipe cards, ensuring smooth navigation through recommended recipes. Additionally, a dynamic loading GIF keeps users engaged while waiting for their recommendations. Furthermore, the ingredient list hover feature provides users with quick insights into recipe details without navigating away from the main interface. These features collectively contribute to a seamless and enjoyable recipe discovery experience for our users.

  ![fried-rice-cooking](https://github.com/NiharikaAdari/Cooking-Mama-Recipe-Recommendations/assets/130190699/0f9b012c-8c2e-4cac-aba3-4401ce725f32)
 
- **OpenAI/ChatGPT Integration:** ChatGPT is used to generate detailed recipes based on user preferences and available ingredients, enhancing the variety and specificity of recipe recommendations.

## Technologies Used

- **Python:** The primary programming language used for web scraping, data processing, and backend development.

- **Flask:** A lightweight web framework for building the web application and handling user requests.

- **Beautiful Soup:** A Python library for pulling data out of HTML and XML files, essential for web scraping.

- **SciKit Learn, Cosine Similarity:** A mathematical technique used to measure the similarity between two non-zero vectors, employed in the recommendation system to compare ingredient lists.

- **OpenAI/ChatGPT:** A powerful natural language processing model used to generate detailed recipes based on user input and preferences.

- **HTML/CSS/JavaScript:** Frontend technologies utilized for designing the user interface and enhancing the user experience.


## Usage
Users can access the Recipe Recommendation App through their web browser. Upon visiting the site, they can input a list of ingredients they have on hand. The app then processes the input, calculates recipe recommendations based on similarity, and displays them along with relevant information such as recipe names, images, and ingredient matches.

## Future Enhancements
- **User Authentication:** Implement user accounts to save favorite recipes and personalize recommendations. If a recipe is chosen, gather real recipe ingredient/cooking process data.
- **Improved Recommendation Algorithm:**: Explore more advanced recommendation algorithms to enhance the accuracy and relevance of recipe suggestions.
- **Enhanced UI/UX:** Continuously improve the user interface and experience to make recipe exploration more intuitive and enjoyable.

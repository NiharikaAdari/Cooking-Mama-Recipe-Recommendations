from flask import Flask, render_template, request
import csv
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai

openai.api_key = ""

app = Flask(__name__)

# Load data from CSV file
# Load data from CSV file
def load_data(csv_file):
    recipes = defaultdict(dict)
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            food_name = row['Food Name']
            ingredients = row['Ingredients']
            image_url = row['Image URL']
            # Find the last occurrence of .jpeg, .png, or .jpg and cut off everything after it
            extensions = ['.jpeg', '.png', '.jpg']
            extension_index = -1
            for ext in extensions:
                ext_index = image_url.rfind(ext)
                if ext_index != -1:
                    extension_index = max(extension_index, ext_index)
            if extension_index != -1:
                image_url = image_url[:extension_index + len(extensions[0])]  # Include the extension
            recipes[food_name]['ingredients'] = ingredients
            recipes[food_name]['image_url'] = image_url
    return recipes






# Preprocess ingredients
def preprocess_ingredients(ingredients):
    tokens = word_tokenize(ingredients.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Calculate Cosine similarity
def calculate_similarity(user_ingredients, recipe_ingredients):
    vectorizer = CountVectorizer()
    ingredients_matrix = vectorizer.fit_transform([user_ingredients, recipe_ingredients])
    cosine_similarities = cosine_similarity(ingredients_matrix)
    return cosine_similarities[1, 0]  # Return the cosine similarity between user input and recipe

# Recommend recipes based on user ingredients
def recommend_recipes(user_ingredients, recipes, top_n=5):
    similarities = []
    for food_name, recipe in recipes.items():
        similarity = calculate_similarity(user_ingredients, recipe['ingredients'])
        similarities.append((food_name, recipe['image_url'], similarity))
    similarities.sort(key=lambda x: x[2], reverse=True)
    return similarities[:top_n]


# Update the similarity_count function to calculate the count directly
def similarity_count(user_input, recipe_ingredients):
    user_ingredients = set(ingredient.strip().lower() for ingredient in user_input.split(','))
    print(user_ingredients)
    recipe_ingredients_list = recipe_ingredients.lower().split('\n')
    count = sum(1 for ingredient in recipe_ingredients_list if ingredient.strip() in user_ingredients)
    return count, len(recipe_ingredients_list)


# Load data
recipes = load_data('food_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []    
    if request.method == 'POST':
        user_input = request.form['ingredients']
        recommendations = recommend_recipes(user_input, recipes)
        similarity_counts = {}
        for recipe in recommendations:
            recipe_name = recipe[0]
            recipe_ingredients = recipes[recipe_name]['ingredients']
            similarity_counts[recipe_name] = similarity_count(user_input, recipe_ingredients)
        recommendations_exist = bool(recommendations)  # Check if recommendations exist
        return render_template('index.html', user_input=user_input, recommendations=recommendations, recipes=recipes, similarity_counts=similarity_counts, recommendations_exist=recommendations_exist)
    return render_template('index.html', recommendations_exist=False)  # Render template with recommendations_exist set to False initially


@app.route('/recipe/<recipe_name>')
def recipe(recipe_name):

    ingredients = recipes[recipe_name]['ingredients']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful cooking assistant that provides cooking recipes and instructions, like cooking mama."},
            {"role": "user", "content": f"Recipe Name: [{recipe_name}]\nMain ingredients: [{ingredients}]"},
            {"role": "system", "content": "give detailed cooking instructions for the recipe."}
        ]
    )
    # Extracting the text from the response's 'choices' might differ slightly, so adjust accordingly
    recipe_instructions = response['choices'][0]['message']['content']    




    return render_template('recipe.html', recipe_name=recipe_name, ingredients=ingredients, recipe_instructions=recipe_instructions)




if __name__ == '__main__':
    app.run(debug=True)

import requests
from bs4 import BeautifulSoup
import csv

def scrape_food_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the food items
    food_items = soup.find_all('div', class_='wikia-gallery-item')

    # Create a CSV file to store the scraped data
    with open('food_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Food Name', 'Image URL', 'Ingredients'])
        
        # Iterate through each food item
        for food in food_items:
            # Extract food name
            food_name = food.find('div', class_='lightbox-caption accent').find('b').text.strip()
            
            # Extract image URL
            image_url = food.find('img').get('data-src') or food.find('img').get('src')
            
            # Extract food page URL
            food_page_url = "https://cookingmama.fandom.com" + food.find('a')['href']
            
            # Send a GET request to the food page URL
            food_page_response = requests.get(food_page_url)
            food_page_soup = BeautifulSoup(food_page_response.text, 'html.parser')
            
            # Find the section containing ingredients
            ingredients_section = food_page_soup.find('span', {'id': 'Ingredients'})
            
            # Extract ingredients if the section is found
            if ingredients_section:
                # Find the <ul> element containing ingredients
                ingredients_list = ingredients_section.find_next('ul')
                
                # Extract individual ingredients from <li> elements
                ingredients = [ingredient.text.strip() for ingredient in ingredients_list.find_all('li')]
                
                # Convert the list of ingredients to a string
                ingredients_str = '\n'.join(ingredients)
            else:
                ingredients_str = "Ingredients not found"
            
            # Write data to CSV file
            writer.writerow([food_name, image_url, ingredients_str])

# URL of the wiki page
url = 'https://cookingmama.fandom.com/wiki/Foods'

# Call the function to scrape data
scrape_food_data(url)

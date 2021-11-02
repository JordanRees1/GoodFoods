# BBC Good Foods shopping list creator
# Takes URLs of recieps and returns a formatted shopping list

# Take the recipes from a file
# what happens if key isn't given

import re
import requests
import jellyfish
from bs4 import BeautifulSoup

# Get recipe list from file
def get_recipes():
    return open('BBC Good Foods/recipes.txt').readlines()

def get_webpage(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_recipe_name(soup):
    return soup.find(class_="post-header__title post-header__title--masthead-layout heading-1").get_text()

# Get the ingredients and return all as a list
def get_ingredients(soup):
    ingredients = soup.find_all(class_="pb-xxs pt-xxs list-item list-item--separator")
    items = [item.get_text().split(',')[0] for item in ingredients]
    return items

def write_shopping_list(line):
    f = open('BBC Good Foods/shopping_list.txt', "a")
    f.write(line+'\n')
    f.close()

recipes = get_recipes()
ingredient_dict = {}
for recipe in recipes:
    soup = get_webpage(recipe)
    ingred = get_ingredients(soup)

    for item in ingred:
        # Remove any whitespace at the end of the string
        item = item.rstrip()
        # Get the number amount at the start of the string 
        amount = re.search("([\d]+)", item)

        rest = re.findall("([^\d]+)", item)

        if not item in ingredient_dict:
            if amount:
                ingredient_dict[item] = int(amount.group(0))
            else:
                ingredient_dict[item] = 1
        else:
            if amount:
                ingredient_dict[item] += int(amount.group(0))
            else:
                ingredient_dict[item] += 1

with open('BBC Good Foods/shopping_list.txt', 'a') as f:
    for key, value in ingredient_dict.items():
        print(value,key, file=f)

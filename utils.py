import requests
from apikey import get_api_key
from Recipe import Recipe


def get_json(query):
    """ingredients=apples,+flour"""
    query = "ingredients="+query
    api_key = '&apiKey=' + get_api_key()
    number_of_result = '&number=1'
    ending = 'findByIngredients?'
    base_url = 'https://api.spoonacular.com/recipes/' + ending + query + number_of_result + api_key
    response = requests.get(base_url).json()
    return response


def parse_json(response):
    recipe_list = []
    for r in response:
        missing_ingredient_list = []
        missed_ingredients = r['missedIngredients']
        title = r['title']
        image = r['image']
        for i in range(len(missed_ingredients)):
            missing_ingredient_list.append(missed_ingredients[i]['name'])
        recipe_object = Recipe(title, image, missing_ingredient_list)
        recipe_list.append(recipe_object)
    return recipe_list


def convert_string_to_list(s):
    return s.split(",")


# Convert a comma separated string to a more suitable input for the API
def format_input(s):
    lst = s.split(",")
    index = 0
    for i in lst:
        if i == ',':
            lst[index + 1] = ''
        index = index+1
    return lst

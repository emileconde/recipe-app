import requests
from apikey import get_api_key
from Recipe import Recipe


def get_json():
    query = 'ingredients=apples,+flour,+sugar'
    api_key = '&apiKey=' + get_api_key()
    number_of_result = '&number=2'
    ending = 'findByIngredients?'
    base_url = 'https://api.spoonacular.com/recipes/' + ending + query + number_of_result + api_key
    response = requests.get(base_url).json()
    return response


def parse_json(response):
    index = 1
    recipe_dict = {}
    for r in response:
        missing_ingredient_list = []
        missed_ingredients = r['missedIngredients']
        title = r['title']
        image = r['image']
        for i in range(len(missed_ingredients)):
            missing_ingredient_list.append(missed_ingredients[i]['name'])
        recipe_object = Recipe(title, image, missing_ingredient_list)
        recipe_dict[index] = [recipe_object.name, recipe_object.image, recipe_object.missed_ingredients]
        index = index + 1
    return recipe_dict


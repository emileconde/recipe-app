import requests
from apikey import get_api_key

query = '?ingredients=apples,+flour,+sugar'
api_key = '&apiKey='+get_api_key()
number_of_result = '&number=10'
ending = 'findByIngredients?'
# base_url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2&apiKey={api_key}'
base_url = 'https://api.spoonacular.com/recipes/'+ending+query+number_of_result+api_key
response = requests.get(base_url)

print(response.json())
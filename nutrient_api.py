import requests
import os
def get_information(infor):
    API_ID = os.environ.get('NUTRIENT_API_ID')
    API_KEY = os.environ.get('NUTRIENT_API_KEY')
    header = {
        'Content-Type' : 'application/json',
        'x-app-id' : API_ID,
        'x-app-key' : API_KEY
    }
    nutrient_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    nutrient_param = {
        'query' : infor
    }
    response = requests.post(url = nutrient_endpoint,json=nutrient_param,headers = header)
    return response.json()
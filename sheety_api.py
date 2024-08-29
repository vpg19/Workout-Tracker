import requests
import os
from datetime import datetime 
from nutrient_api import *
def add_workout(info):
    sheety_endpoint = 'https://api.sheety.co/1f2cc20a52ec05d7f36d7d67a102bd7e/myWorkouts/workouts'
    basic_header = {
        'Authorization' : os.environ.get('SHEETY_AUTH_KEY')
    }
    data = get_information(info)
    date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    for i in data['exercises']:
        sheety_params = {
            'workout' : {
                'date' : date,
                'time' : now_time,
                'exercise' : i['name'].title(),
                'duration' : i['duration_min'],
                'calories' : i['nf_calories']
            }
        }
        response = requests.post(url=sheety_endpoint,json = sheety_params,headers = basic_header)
        print(response.text)

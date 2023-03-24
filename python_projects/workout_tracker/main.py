import requests
import datetime as dt
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")


nutrition_endpoint = os.environ.get("Nutrition_Endpoint")

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_parameters = {
    "query": input("What exercises did you do? "),
    "gender": "male",
    "weight_kg": 83.92,
    "height_cm": 181,
    "age": 26
}

user_exercise = requests.post(url=nutrition_endpoint, headers=HEADER, json=exercise_parameters)
user_exercise.raise_for_status()
exercise_data = user_exercise.json()["exercises"]

today = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

token = os.environ.get("TOKEN")
exercise_token = {"Authorization": f"Bearer {token}"}

for exercise in exercise_data:
    sheet_input = {
            "workout": {
                "date": today,
                "time": now_time,
                "exercise": exercise_data[0]['user_input'].title(),
                "duration": exercise_data[0]['duration_min'],
                "calories": exercise_data[0]['nf_calories']
            }
        }

    new_row = requests.post(url=sheety_endpoint, json=sheet_input, headers=exercise_token)
    new_row.raise_for_status()
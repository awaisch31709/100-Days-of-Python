import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]
SHEETY_TOKEN = os.environ["TOKEN"]

exercise_text = input("What exercise did you do? ")

nutrition_response = requests.post(
    url="https://app.100daysofpython.dev/v1/nutrition/natural/exercise",
    headers={
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    },
    json={"query": exercise_text},
)
nutrition_response.raise_for_status()
result = nutrition_response.json()

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

now = datetime.now()

for exercise in result["exercises"]:
    row_data = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=row_data,
        headers=sheety_headers,
    )
    sheety_response.raise_for_status()
    print(f"Saved {exercise['name']} to My Workouts.")
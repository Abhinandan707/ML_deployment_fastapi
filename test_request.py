import json
import requests

data = {"age": 45,
        "workclass": "Self-emp-inc",
        "fnlgt": 287927,
        "education": "HS-grad",
        "education_num": 9,
        "marital_status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Wife",
        "race": "White",
        "sex": "Female",
        "capital_gain": 5024,
        "capital_loss": 0,
        "hours_per_week": 45,
        "native_country": "United-States"
        }

response = requests.post(
    "http://127.0.0.1:8080/predict", data=json.dumps(data))

print(response.status_code)
print(response.json())
from fastapi.testclient import TestClient
import os
import sys
import json

root_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(root_dir)

from main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == "Welcome boss!"


def test_predict_positive():
    data = {"age": 45,
            "workclass": "Self-emp-inc",
            "fnlgt": 3832127,
            "education": "HS-grad",
            "education_num": 7,
            "marital_status": "Married-civ-spouse",
            "occupation": "Exec-managerial",
            "relationship": "Wife",
            "race": "White",
            "sex": "Female",
            "capital_gain": 99999,
            "capital_loss": 111,
            "hours_per_week": 41,
            "native_country": "United-States"
            }
    response = client.post("/predict", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json() == {"pred": ">50K"}


def test_predict_negative():
    data = {"age": 39,
            "workclass": "State-gov",
            "fnlgt": 60516,
            "education": "Bachelors",
            "education_num": 9,
            "marital_status": "Never-married",
            "occupation": "Adm-clerical",
            "relationship": "Not-in-family",
            "race": "White",
            "sex": "Male",
            "capital_gain": 200,
            "capital_loss": 0,
            "hours_per_week": 35,
            "native_country": "United-States"
            }
    response = client.post("/predict", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json() == {"pred": "<=50K"}


def test_predict_invalid():
    data = {}
    response = client.post("/predict", json=json.dumps(data))
    assert response.status_code == 422
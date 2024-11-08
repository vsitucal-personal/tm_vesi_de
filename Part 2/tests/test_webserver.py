import json
from fastapi.testclient import TestClient
from app.main import Webserver
from unittest.mock import MagicMock
from app.models.model import CheckinsModel
from datetime import datetime

webserver = Webserver()
client = TestClient(webserver.app)


def test_read_root():
    # Send a GET request to the root endpoint
    response = client.get("/")
    # Assert the status code is 201
    assert response.status_code == 201
    # Assert the response JSON is correct
    assert response.json() == {"message": "Hi from root"}


def test_get_checkins():
    now = datetime.now()
    webserver.db.get_checkins_records = MagicMock(return_value=(
        [CheckinsModel(user="testuser", date=now.date(), project="xxx", hours=4.5)], 1
    ))
    webserver.db.get_checkins_count = MagicMock(return_value=1)

    # Define example query parameters for the test
    params = {
        "user": "testuser",
        "page": 1,
        "page_size": 10
    }

    # Send a GET request to the /checkins endpoint with query parameters
    response = client.get("/checkins", params=params)

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response matches the expected schema and content
    expected_response = {
        "total_count": 1,
        "returned_count": 1,
        "max_page": 1,
        "page": 1,
        "records": [
            json.loads(CheckinsModel(user="testuser", date=now.strftime("%Y-%m-%d"), project="xxx", hours=4.5).json())
        ]
    }
    assert response.json() == expected_response

    # Verify that the mock methods were called with the expected arguments
    webserver.db.get_checkins_records.assert_called_with("testuser", 1, 10)
    webserver.db.get_checkins_count.assert_called_with("testuser")


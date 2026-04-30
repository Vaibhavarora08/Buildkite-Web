import pytest
from app import app          # import your Flask app like a normal Python module

# This is a pytest "fixture" - think of it as setup code
# It creates a test version of your app before each test runs
@pytest.fixture
def client():
    app.config["TESTING"] = True   # puts Flask in test mode (better error messages)
    with app.test_client() as client:
        yield client               # yield is like return but keeps the connection open

# Each function starting with test_ is automatically picked up by pytest

def test_home_page(client):
    response = client.get("/")            # simulate a browser visiting /
    assert response.status_code == 200    # 200 = OK in HTTP (like a thumbs up)
    assert b"Hello from Buildkite" in response.data  # b"..." = bytes, not string

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()       # parse the JSON response
    assert json_data["status"] == "ok"

def test_greet_with_name(client):
    response = client.get("/greet/Vaibhav")
    assert response.status_code == 200
    assert b"Vaibhav" in response.data    # check the name appears in the page
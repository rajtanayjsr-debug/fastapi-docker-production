import requests

BASE_URL = "http://localhost:8000"


def test_route(route):
    url = BASE_URL + route

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"PASS: {route} -> Status {response.status_code}")
            print("Response:", response.json())
        else:
            print(f"FAIL: {route} -> Status {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"ERROR: {route} -> {error}")


print("Starting Automated API Testing...\n")

test_route("/")
test_route("/health")
test_route("/students")

print("\nAutomated Testing Completed.")
import requests
import json

# --- CONFIGURATION ---
# We're using JSONPlaceholder, a free fake API for testing.
API_URL = "https://jsonplaceholder.typicode.com"

# --- PART 1: GET Request (Reading data) ---

def fetch_data():
    """
    Performs a GEt request to fetch posts from the API.
    :return:
    """
    print("--- Running GET Request ---")
    try:
        # Get the list of "posts" - we can add '/1' to get just the first post.
        response = requests.get(f"{API_URL}/posts/1")

        # Always check the status code:
        # 200 = OK
        # 404 = Not Found
        # 500 = Server Error
        response.raise_for_status() # Raisea an error if the status code is not 2xx

        print("GET request successful (Status Code 200).")

        # .json() is a requests helper that auto-converts the JSON text
        # into a Python dictionary.
        data = response.json()

        print("\nSuccessfully parsed JSON response.")
        # 'json.dumps' formats the Python dictionary to print pretty
        print(json.dumps(data, indent=2))

        # We can now access items like a dictionary
        print(f"\nTitle of past #1: {data['title']}'")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#--- PART 2: POST Request (writing data) ---

def post_test_result():
    """
    Performs a POST request to simulate saving a new test result.
    :return:
    """
    try:
        # This is the data we are "uploading".
        new_result_data = {
            'title': 'Test Run 101',
            'body': 'Potentiometer test complete. All values nominal.',
            'userId': 1
        }

        # Send our data as the 'json' parameter.
        # request will auto-format it as JSON.
        response = requests.post(f"{API_URL}/posts", json=new_result_data)

        # Check the status code - a successful POST is often '201  Created'
        response.raise_for_status()

        print(f"POST request successful (Status Code {response.status_code}).")

        # The API replies with the new object it created, including its new ID
        created_data = response.json()

        print(f"Successfully posted new data. Server responded with:")
        print(json.dumps(created_data, indent=2))
        print(f"\nOur new data was assigned ID: {created_data['id']}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    fetch_data()
    post_test_result()
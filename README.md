# Python API Client (Requests)

this script demonstrates how to use the 'requests' library in Python to interact with a public REST API.

## Features

* **GET Request:** Fetches data for a single post from the `jsonplaceholder` fake API.
* **POST Request:** Simulates uploading a new "test result" (a new post) to the API.
* **Error Handling:** Uses `try...except` blocks and `response.raise_for_status()` to properly handle HTTP and connection errors.
* **JSON Handling:** Uses the `response.json()` method to parse server responses into Python dictionaries and `json.dumps()` for pretty-printing.
* 
## How to Use

1.  Clone this repository and create a virtual environment.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ensure you have an active internet connection.
4.  Run the script:
    ```bash
    python api_client.py
    ```
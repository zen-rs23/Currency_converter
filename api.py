import requests

BASE_URL = "https://www.frankfurter.app"

def get(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for HTTP errors
    return response.json()
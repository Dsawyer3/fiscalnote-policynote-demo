import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    api_key = os.getenv("POLICYNOTE_API_KEY")
    response = requests.post(
        "https://data.policynote.com/v1/auth/token",
        headers={"x-api-key": api_key}
    )
    response.raise_for_status()
    return response.json()["access_token"]

if __name__ == "__main__":
    token = get_access_token()
    print("Got token:", token)
from auth import get_access_token
import requests

def search_legislation(query, limit=20):
    token = get_access_token()
    response = requests.get(
        "https://data.policynote.com/v1/legislation/search",
        headers={"Authorization": f"Bearer {token}"},
        params={"query_string": query, "limit": limit}
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = search_legislation("artificial intelligence chatbot minor")
    print("Total results:", data["estimated_total_results"])
    print("Bills returned:", len(data["results"]))
    for item in data["results"]:
        bill = item["bill"]
        print("-", bill["primary_external_id"], ":", bill["title"])
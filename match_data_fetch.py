import requests
import json
from rich import print  # Rich's print supports colors
from rich.pretty import Pretty
import logging
import httpx
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_detail_live():
    """
    Fetch data from the detail_live endpoint.

    Returns:
        dict: The JSON response containing match details.
    """
    url = "https://api.thesports.com/v1/football/match/detail_live"
    params = {
        "user": "thenecpt",
        "secret": "0c55322e8e196d6ef9066fa4252cf386"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching detail_live data: {e}")
        return None

# Function to fetch match IDs
def fetch_match_ids():
    data = fetch_detail_live()
    if data:
        return [result['id'] for result in data.get('results', []) if result.get('id') and data.get('code') == 0]
    return []

# Asynchronous function to fetch data for a single match ID
async def fetch_data_for_id(client, match_id):
    base_url = "https://api.thesports.com/v1/football/match/recent/list"
    user = "thenecpt"
    secret = "0c55322e8e196d6ef9066fa4252cf386"
    url = f"{base_url}?user={user}&secret={secret}&uuid={match_id}"

    try:
        response = await client.get(url)
        response.raise_for_status()
        return {"id": match_id, "data": response.json()}
    except httpx.RequestError as e:
        return {"id": match_id, "error": str(e)}

# Asynchronous function to fetch data for all match IDs
async def fetch_all_match_details(match_ids):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_data_for_id(client, match_id) for match_id in match_ids]
        return await asyncio.gather(*tasks)

def filter_match_data(match_data):
    filtered_data = {}
    for key, value in match_data.items():
        # Skip fields to be removed
        if key in ["venue_id", "season_id", "note", "coverage", "round", "referee_id"]:
            continue
        # Skip fields whose values are arrays (lists)
        if isinstance(value, list):
            continue
        # Add remaining fields to the filtered data
        filtered_data[key] = value
    return filtered_data

if __name__ == "__main__":
    match_ids = fetch_match_ids()
    if match_ids:
        print(f"Fetched Match IDs: {match_ids}")
        detailed_data = asyncio.run(fetch_all_match_details(match_ids))

        # Filter the detailed match data
        filtered_results = []
        for match in detailed_data:
            if "data" in match and "results" in match["data"]:
                for result in match["data"]["results"]:
                    filtered_results.append(filter_match_data(result))

        print("Filtered Match Data:")
        print(filtered_results)
    else:
        print("No match IDs fetched.")
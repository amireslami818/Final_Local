#!/usr/bin/env python3
import requests
import json
import httpx
from rich import print  # Rich's print supports colors
from rich.pretty import Pretty

# Hard-coded credentials
USER = "thenecpt"
SECRET = "0c55322e8e196d6ef9066fa4252cf386"

# Base URL for the detail_live endpoint
BASE_URL = "https://api.thesports.com/v1/football/match/detail_live"

def fetch_detail_live():
    """
    Fetch data from the detail_live endpoint.
    
    Global parameters:
      - user: Username for API access.
      - secret: Key provided for verification.
      
    Expected response structure:
      {
          "code": <status code>,
          "results": <data content>
      }
      
    Returns:
      The response JSON data as a Python dictionary.
    """
    params = {
        "user": USER,
        "secret": SECRET
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes.
        data = response.json()       # Parse response to JSON.
        return data
    except requests.RequestException as e:
        print(f"[bold red]Error fetching detail_live data:[/bold red] {e}")
        return None

def remove_nested_fields(data):
    """
    Iterate over each match and remove specific nested fields if they exist.
    
    Args:
        data (dict): The JSON data containing match information.

    Returns:
        dict: The modified JSON data with specified fields removed.
    """
    for match in data.get("results", []):
        for incident in match.get("incidents", []):
            # Remove the specified nested fields if they exist
            incident.pop("in_player_id", None)
            incident.pop("in_player_name", None)
            incident.pop("out_player_id", None)
            incident.pop("out_player_name", None)
    return data

def remove_fields(data):
    """
    Removes the `stats`, `incidents`, and `tlive` fields from each match object.
    """
    for match in data.get("results", []):
        match.pop("stats", None)
        match.pop("incidents", None)
        match.pop("tlive", None)
    return data

def fetch_data():
    url = "https://example.com/api/endpoint"  # Replace with your endpoint
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Assuming the response is in JSON format
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting: {exc}")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url}")

def standardize_match_score(match):
    """
    Standardizes the match score representation for a given match object.

    Args:
        match (dict): A match object containing the `score` array.

    Returns:
        str: A standardized score string in the format:
             "[HomeLive]-[AwayLive] (HT: [HomeHT]-[AwayHT])"
    """
    score = match.get("score", [])
    if len(score) < 4:
        return "Invalid score data"

    home_team_array = score[2]  # Home team score array
    away_team_array = score[3]  # Away team score array

    if len(home_team_array) < 2 or len(away_team_array) < 2:
        return "Invalid score data"

    home_live = home_team_array[0]  # Home team live score
    home_ht = home_team_array[1]    # Home team half-time score
    away_live = away_team_array[0]  # Away team live score
    away_ht = away_team_array[1]    # Away team half-time score

    return f"{home_live}-{away_live} (HT: {home_ht}-{away_ht})"

def main():
    data = fetch_detail_live()
    if data is None:
        return

    # Remove specified nested fields and fields
    data = remove_nested_fields(data)
    data = remove_fields(data)

    # Standardize scores for each match and update the JSON structure
    for match in data.get("results", []):
        standardized_score = standardize_match_score(match)
        match["standardized_score"] = standardized_score

    # Print each match in the requested format
    print("[bold blue]\nMatch Details:[/bold blue]")
    for match in data.get("results", []):
        timestamp = match.get("score", [])[4]  # Extract the timestamp value
        print("[bold cyan]MATCH ID:[/bold cyan]", match.get("id"))
        print("[bold magenta]SCORE:[/bold magenta]", match.get("standardized_score"))
        print("[bold green]TIME STAMP:[/bold green]", timestamp)
        print("\n")

    # Count the number of live games (match datasets) and print at the bottom
    total_live_games = len(data.get("results", []))
    print(f"[bold yellow]Total Live Games:[/bold yellow] {total_live_games}\n")

if __name__ == "__main__":
    main()
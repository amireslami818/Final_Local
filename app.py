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

def main():
    data = fetch_detail_live()
    if data is None:
        return

    # Print the raw JSON data (as a string, indented)
    print("[bold green]Raw JSON Data:[/bold green]")
    print(json.dumps(data, indent=4))

    # Pretty-print the JSON data using Rich's Pretty component
    print("[bold blue]\nPretty Printed JSON (with color):[/bold blue]")
    print(Pretty(data))

    # Example usage of fetch_data
    example_data = fetch_data()
    if example_data:
        print(example_data)

if __name__ == "__main__":
    main()

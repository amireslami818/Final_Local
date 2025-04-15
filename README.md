# Updated the README to include information about filtering and removing properties from JSON objects.

## JSON Filtering and Removal

### Task: Filter and Remove Properties from JSON Objects

The following updates were made to the `app.py` script:

1. **Filter and Remove Properties from the 'stats' Array**:
   - All properties (key-value pairs) from the JSON objects within the 'stats' array were removed.
   - This ensures that the 'stats' array is now empty for each match object.

2. **Filter and Remove Properties from the 'stats' Array**:
   - All properties (key-value pairs) from the JSON objects within the 'stats' array were removed.
   - This ensures that the 'stats' array is now empty for each match object.

3. **Filter and Remove Properties from the 'corner' Array**:
   - All properties (key-value pairs) from the JSON objects within the 'corner' array were removed.
   - This ensures that the 'corner' array is now empty for each match object.

### Implementation Details

- The `remove_stats_properties` function was added to iterate over each match object and clear the 'stats' array.
- The function is called within the `main` function to process the fetched JSON data.

### Example

Before:
```json
"stats": [
    {"type": 3, "home": 0, "away": 1},
    {"type": 23, "home": 21, "away": 37}
]
```

After:
```json
"stats": []
```

Before:
```json
"corner": [
    {"type": 1, "position": 1, "time": 7},
    {"type": 3, "position": 2, "time": 20}
]
```

After:
```json
"corner": []
```

### How to Use

Run the `app.py` script to automatically process the JSON data and apply the filtering/removal logic.

# Match Score Standardization

This project processes match data and standardizes the representation of match scores based on fixed positions in the score arrays.

## Parsing Rule

The JSON object includes a key called `score`, which is an array with several elements. The following rules are applied to extract and standardize the match scores:

### Home Team
- **Live Score**: The first element (index 0) of the home team score array (found at index 2 of the `score` array).
- **Half-Time Score**: The second element (index 1) of the home team score array.

### Away Team
- **Live Score**: The first element (index 0) of the away team score array (found at index 3 of the `score` array).
- **Half-Time Score**: The second element (index 1) of the away team score array.

### Standard Formula
The standardized match score is represented as:

```
Live Score: [HomeLive]-[AwayLive] (HT: [HomeHT]-[AwayHT])
```

Where:
- `[HomeLive]` is the first element of the home team score array.
- `[HomeHT]` is the second element of the home team score array.
- `[AwayLive]` is the first element of the away team score array.
- `[AwayHT]` is the second element of the away team score array.

### Example
Given the following JSON structure:

```json
{
  "id": "zp5rzghgyjokq82",
  "score": [
      "zp5rzghgyjokq82",
      4,
      [1, 1, 0, 0, 4, 0, 0],   // Home team score array
      [0, 0, 0, 1, 4, 0, 0],   // Away team score array
      1744668208,
      ""
  ]
}
```

The standardized score would be:

```
Live Score: 1-0 (HT: 1-0)
```

## Implementation
The `standardize_match_score` function in `app.py` processes the match data and applies the above rules to generate the standardized score for each match. The results are stored in the `standardized_score` field of each match object.

## Running the Application
To run the application and see the standardized scores:

1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute the script:
   ```bash
   python3 app.py
   ```

The output will include the raw JSON data with the standardized scores and a count of live matches.

## Code 0 Match IDs

The `match_data_fetch.py` script fetches match data and filters it to retain only the `id` fields associated with `code: 0`. These IDs are referred to as "Code 0 Match IDs."

The script also prints the total number of Code 0 Match IDs fetched.

# Match Data Fetching and Processing

This project fetches match data and processes it in two main steps:

## Step 1: Fetch Match IDs
- The `match_data_fetch.py` script fetches match IDs associated with `code: 0` from the endpoint `https://api.thesports.com/v1/football/match/detail_live`.
- The script lists the fetched IDs and logs the total count.

## Step 2: Fetch Detailed Data for Each Match ID
- Using the fetched match IDs, the script makes asynchronous HTTP requests to the endpoint `https://api.thesports.com/v1/football/match/recent/list`.
- Each match ID is processed individually, and detailed match data is retrieved and displayed.

## Features
- **Asynchronous Requests**: The project uses `httpx` and `asyncio` to fetch detailed match data concurrently, improving efficiency.
- **Logging**: Logs HTTP requests and responses for better traceability.
- **Rich Output**: Uses the `rich` library for pretty-printing data in the terminal.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the `match_data_fetch.py` script:
   ```bash
   python3 match_data_fetch.py
   ```
3. View the fetched match IDs and their detailed data in the terminal.

## Files
- `match_data_fetch.py`: Main script for fetching and processing match data.
- `app.py`: Additional processing logic for match data.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.

## Requirements
- Python 3.10 or higher
- Libraries: `httpx`, `rich`

## Notes
- Ensure the API credentials (`user` and `secret`) are valid and have access to the required endpoints.
- The project is designed to handle large datasets efficiently using asynchronous programming.
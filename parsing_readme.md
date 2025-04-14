# Parsing README

## Overview
This document outlines the parsing and filtering logic implemented in the `app.py` script. The script processes JSON data fetched from an API, applies specific filtering rules, and removes unnecessary fields.

## Key Features
1. **Field Removal**:
   - The `stats`, `incidents`, and `tlive` fields are completely removed from each match object in the JSON data.

2. **Nested Field Removal**:
   - Specific nested fields (`in_player_id`, `in_player_name`, `out_player_id`, `out_player_name`) are removed from the `incidents` array if they exist.

3. **Data Fetching**:
   - The script fetches data from a hardcoded API endpoint (`https://api.thesports.com/v1/football/match/detail_live`) using credentials.

4. **Error Handling**:
   - Handles API request errors gracefully and logs them for debugging.

## Functions
### `fetch_detail_live()`
Fetches data from the `detail_live` API endpoint using hardcoded credentials.

### `remove_nested_fields(data)`
Iterates over each match object and removes specific nested fields from the `incidents` array.

### `remove_fields(data)`
Removes the `stats`, `incidents`, and `tlive` fields entirely from each match object.

### `fetch_data()`
Fetches data from an example endpoint (`https://example.com/api/endpoint`) and handles request errors.

### `main()`
Coordinates the execution of the script:
1. Fetches data from the API.
2. Applies the nested field removal logic.
3. Removes the `stats`, `incidents`, and `tlive` fields.
4. Prints the processed JSON data.

## Example Output
After processing, the JSON data will look like this:
```json
{
    "code": 0,
    "results": [
        {
            "id": "pxwrxlh5dwkjryk",
            "score": [
                "pxwrxlh5dwkjryk",
                2,
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                1744671553,
                ""
            ]
        },
        {
            "id": "jw2r09hk404nrz8",
            "score": [
                "jw2r09hk404nrz8",
                2,
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                1744671548,
                ""
            ]
        }
        // ...additional match objects...
    ]
}
```

## Error Handling
- Logs errors if the API request fails or times out.
- Ensures the script continues running even if some operations fail.

## Usage
1. Run the script using:
   ```bash
   python3 app.py
   ```
2. The processed JSON data will be printed to the console.

## Dependencies
- `requests`
- `httpx`
- `rich`

Install dependencies using:
```bash
pip install -r requirements.txt
```
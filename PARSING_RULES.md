# Parsing Rules

This document outlines the parsing and filtering rules applied to the match data in this project.

## Match Score Standardization

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

## Filtering Rules

### Removing Nested Fields
Specific nested fields are removed from the `incidents` array in each match object:
- `in_player_id`
- `in_player_name`
- `out_player_id`
- `out_player_name`

### Clearing Arrays
The following arrays are cleared of all properties:
- `stats`
- `corner`
- `incidents`
- `tlive`

### Removing Specific Fields
The following fields are removed entirely from each match object if they exist:
- `tlive`
- `corner`
- `incidents`
- `stats`

### Example
Before:
```json
{
  "stats": [
      {"type": 3, "home": 0, "away": 1},
      {"type": 23, "home": 21, "away": 37}
  ],
  "corner": [
      {"type": 1, "position": 1, "time": 7},
      {"type": 3, "position": 2, "time": 20}
  ]
}
```

After:
```json
{
  "stats": [],
  "corner": []
}
```

## Implementation
The parsing and filtering rules are implemented in the following functions in `app.py`:

- `standardize_match_score`: Standardizes the match score representation.
- `remove_nested_fields`: Removes specific nested fields from the `incidents` array.
- `remove_stats_properties`: Clears all properties from the `stats` array.
- `remove_corner_properties`: Clears all properties from the `corner` array.
- `remove_incidents_properties`: Clears all properties from the `incidents` array.
- `remove_empty_fields_and_tlive_properties`: Removes empty fields and clears the `tlive` array.
- `remove_specified_fields`: Removes the `tlive`, `corner`, and `incidents` fields entirely.
- `remove_stats_field`: Removes the `stats` field entirely.
import requests
import json

# Define the API endpoint URL
api_url = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"

# Send an HTTP GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    
    # Now, 'data' contains the JSON response from the ESPN API, and you can work with the data as needed.
    
    # For example, you can print the data to see the structure

    the_game = None
    unc_score = None
    awayteam_score = None

    # Search for UNC game in list of college games received from ESPN api
    for game in data["events"]:
        if "UNC" in game["shortName"]:
            the_game = game

    # Search for UNC score and away score in the game
    for score in the_game["competitions"][0]["competitors"]:
        if "UNC" in score["team"]["abbreviation"]:
            unc_score = score["score"]
        else:
            awayteam_score = score["score"]

    current_scores = {
        "unc_score": unc_score,
        "awayteam_score": awayteam_score
    }

    with open('data.json', 'w') as json_file:
        json.dump(current_scores, json_file)

else:
    # If the request was not successful, print an error message
    print("Failed to retrieve data. Status code:", response.status_code)

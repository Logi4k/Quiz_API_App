# Import requests module
import requests

# Set parameters for API request
parameters = {
    "amount": 10,  # number of questions to retrieve
    "type": "boolean",  # type of questions to retrieve
}

# Make request to API
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# Raise exception if request was unsuccessful
response.raise_for_status()

# Get JSON data from API response
data = response.json()

# Get list of question data from API response
question_data = data["results"]

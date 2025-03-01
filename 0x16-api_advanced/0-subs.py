#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "alx-api-advanced/1.0"}

    # Construct the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data["data"]["subscribers"]
            return subscribers
        except (KeyError, ValueError):
            # Handle cases where the JSON structure is unexpected
            return 0
    else:
        # Handle cases where the subreddit is invalid or other errors occur
        return 0

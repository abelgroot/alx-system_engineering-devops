#!/usr/bin/python3
"""
Module to query the Reddit API and print the titlesof
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints the titles or None if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "alx-api-advanced/1.0"}

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the list of posts
            posts = data["data"]["children"]
            # Print the titles of the first 10 posts
            for post in posts:
                print(post["data"]["title"])
        except (KeyError, ValueError):
            # Handle cases where the JSON structure is unexpected
            print(None)
    else:
        # Handle cases where the subreddit is invalid or other errors occur
        print(None)

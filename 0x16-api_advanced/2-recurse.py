#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a
list of titles of all hot posts for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list
    of titles of all hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot post titles (used for recursion).
        after (str): The pagination token for the next page of results.

    Returns:
        list: A list of hot post titles.
        Returns None if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "alx-api-advanced/1.0"}

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    # Make the API request
    response = requests.get(
        url, headers=headers,
        params=params,
        allow_redirects=False
    )

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the list of posts
            posts = data["data"]["children"]
            # Add the titles of the posts to the hot_list
            for post in posts:
                hot_list.append(post["data"]["title"])
            # Check if there is another page of results
            after = data["data"]["after"]
            if after:
                # Recursively call the function to fetch the next page
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the hot_list
                return hot_list
        except (KeyError, ValueError):
            # Handle cases where the JSON structure is unexpected
            return None
    else:
        # Handle cases where the subreddit is invalid or other errors occur
        return None

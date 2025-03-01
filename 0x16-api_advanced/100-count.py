#!/usr/bin/python3
"""
Module to recursively query the Reddit API, count keywords
in hot post titles, and print the results.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, counts keywords in
    hot post titles, and prints the results.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.
        after (str): The pagination token for the next page of results.
        counts (dict): A dictionary to store keyword
        counts (used for recursion).

    Returns:
        None: Prints the results or nothing if no matches or invalid subreddit.
    """
    if counts is None:
        counts = {}

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "alx-api-advanced/1.0"}

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    # Make the API request
    response = requests.get(
        url,
        headers=headers,
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
            # Iterate through the posts
            for post in posts:
                title = post["data"]["title"].lower()
                # Count occurrences of each keyword in the title
                for word in word_list:
                    word_lower = word.lower()
                    # Count whole words only
                    count = title.split().count(word_lower)
                    if word_lower in counts:
                        counts[word_lower] += count
                    else:
                        counts[word_lower] = count
            # Check if there is another page of results
            after = data["data"]["after"]
            if after:
                # Recursively call the function to fetch the next page
                return count_words(subreddit, word_list, after, counts)
            else:
                # No more pages, sort and print the results
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        except (KeyError, ValueError):
            # Handle cases where the JSON structure is unexpected
            pass
    else:
        # Handle cases where the subreddit is invalid or other errors occur
        pass

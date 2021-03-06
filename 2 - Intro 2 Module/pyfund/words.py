
#!/usr/bin/env python3
"""
Basic script to retrieve and print words from a URL

Author: Pierre Baudin
Date: 2018-10-19

Usage: 

    python3 words.py <URL>

Note: can be update and modify by adding encoding to  utf-8 for better performance
"""

# Import packages libraries
from urllib.request import urlopen
import sys


# define fetch_word function
def fetch_words(url):
    """
    Fetch a list of words from a URL
    
    Args:
        url: the url of any text document (no decoding to utf-8 added)
    
    Returns:
        A list of strings containing the words in the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


# function to print imported website
def print_items(items):
    """
    Print items on per line

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)


# def main function
def main(url):
    """
    Print each word from a text document

    Args:
        url: the URL of any website
    """
    words = fetch_words(url)
    print_items(words)


# Module execution 
if __name__ == "__main__":
    main(sys.argv[1]) # the 0th arg is the module filename
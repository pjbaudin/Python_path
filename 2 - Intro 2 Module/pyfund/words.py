from urllib.request import urlopen
import sys


# define fetch_word function
def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


# function to print imported website
def print_items(items):
    for item in items:
        print(item)


# def main function
def main(url):
    words = fetch_words(url)
    print_items(words)


# Module execution 
if __name__ == "__main__":
    main(sys.argv[1])
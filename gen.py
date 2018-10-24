"""
Module for demonstrating generator execution
"""


def take(count, iterable):
    """
    Take items from the from of an iterable
    :param count:  the maximum number of items to retrieve
    :param iterable: the source series
    :yields: at most 'count' items from 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


if __name__ == '__main__':
    run_take()
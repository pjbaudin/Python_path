"""
A module for demonstrating exceptions.
"""
import sys
from math import log

def convert(s):
    '''
    convert to an integer
    :param s: input
    :return: s as an integer
    '''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
              file=sys.stderr)
        raise

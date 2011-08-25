#!/usr/bin/env python -u

"""
Read in lines from stdin and quote a random word in the line in the
style of Joey from friends.
"""

import sys
import random

def main():
    line = None
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        words = line.split(' ')
        word_to_quote = random.randint(0, len(words) - 1)
        words[word_to_quote] = '"%s"' % words[word_to_quote]
        print " ".join(words)
        
if __name__ == '__main__':
    main()

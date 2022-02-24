#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re


def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        if len(words) > 3:
            if words[0] == "united" and words[1] == "states":
                num, den = words[-1].split('/')
                probability = float(num)/float(den)
                print('%s%s%s,%f' % ("united states", separator, words[2], probability))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

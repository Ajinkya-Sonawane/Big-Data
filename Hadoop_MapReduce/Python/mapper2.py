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
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        str_words = ' '.join(words[:-1])
        value = str_words + "," + words[-1]
        temp_key = len(value.split(' '))
        print('%d%s%s' % (temp_key, separator, value))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

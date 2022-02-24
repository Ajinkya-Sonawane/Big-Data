#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re


def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        line = re.sub('[^0-9a-zA-Z]', ' ', line).lower()
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
        words_len = len(words)
        if words_len >= 3:
            for index in range(words_len):
                print('%s%s%d' % (words[index], separator, 1))
                if index < words_len-1:
                    print('%s%s%d' % (words[index] + " " + words[index+1], separator, 1))
                if index < words_len - 2:
                    print('%s%s%d' % (words[index] + " " + words[index + 1] + " " + words[index + 2], separator, 1))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    res = ''
    max_prob = 0
    for key, group in groupby(data, itemgetter(0)):
        for key_, value in group:
            word, prob = value.split(',')
            if float(prob) > max_prob:
                max_prob = float(prob)
                res = word
        print("Result: united states %s -- with a probability of %f" % (res, max_prob))


if __name__ == "__main__":
    main()

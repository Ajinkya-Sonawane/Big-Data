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


def produce_output(ngram, ngramcnt, separator):
    for gram in ngram:
        val, cnt = gram.split(',')
        print("%s%s%s/%d" % (val, separator, cnt, ngramcnt))


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    unigram = []
    bigram = []
    trigram = []
    for ngram, group in groupby(data, itemgetter(0)):
        for ngram_,value in group:
            if ngram == "1":
                unigram.append(value)
            elif ngram == "2":
                bigram.append(value)
            elif ngram == "3":
                trigram.append(value)
    produce_output(unigram, len(unigram), separator)
    produce_output(bigram, len(bigram), separator)
    produce_output(trigram, len(trigram), separator)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    binary_clasification
    ~~~~~~~~~~~~~~~~~~~~

    Load a yaml file with results of a binary classfication and prints Confusion
    matrix for that results.

    Example of a file of an application that detects language of documents: ::

        # Languages that can be detected
        types: [en, es, pt, it, de]
        # it's cosidered a hit if result is less than umbral
        umbral: 0.5
        sample: 
          - result:
              en: 0.88
              es: 0.7
              pt: 0.98
              it: 0.6666  # is not a hit! ( 0.6666 > 0.5 )
              de: 0.3 # hit
            expected: de
          - result:
              en: 0.88
              es: 0.1 # hit
              pt: 0.98
              it: 0.6666
              de: 0.3 # hit
            expected: es


    :copyright: (c) 2011 by  Miguel Olivares and F.Javier Alba.
"""
from confumatrix import ConfuMatrix


import os.path
import sys
import yaml


def usage():
    return 'Usage: binary_classification.py yaml_input_file'


def load_sample(sample_file):
    with open(sample_file, 'r') as fd:
        return yaml.safe_load(fd.read())


def main():
    # Check params
    if len(sys.argv) != 2:
        print usage()
        sys.exit(2)
    if not os.path.exists(sys.argv[1]):
        print 'Invalid input file'
        sys.exit(2)
    
    sample_file = sys.argv[1]

    sample = None
    try:
        sample = load_sample(sample_file)
    except:
        print 'Invalid format. Be sure is yaml format'
        sys.exit(2)

    result = {}
    for ty in sample['types']:
        result[ty] = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}

    for case in sample['sample']:
        # Expected value for current case
        expected = case['expected']
        # Resulted values for current case
        resulted = [k for k, v in case['result'].items() if v > sample['umbral']]
        for ty in sample['types']:
            if expected == ty:
                if expected in resulted:
                    result[ty]['a'] += 1
                else:
                    result[ty]['c'] += 1
            else:
                if ty in resulted:
                    result[ty]['b'] += 1
                else:
                    result[ty]['d'] += 1

    # print results
    for ty in sample['types']:
        print ty
        print ConfuMatrix(**result[ty])


def caption():
    print '%s\n' % ('=' * 25)
    print '%s Help %s\n' % ('-' * 10, '-' * 10)
    print 'Confusion Matrix:\n'
    print '\t\tTrue\t\tFalse'
    print 'Positive:\tTrue positive\tfalse negative'
    print 'Negative:\tfalse negative\tTrue negative\n\n'
    print 'Accuracy: degree of veracity'
    print 'Precision: degree of reproducibility'
    print 'Recall (or Sensitivity): proportion of actual positives which are correctly identified as such'
    print 'Specificity: proportion of negatives which are correctly identified'
    print 'F-measure: single measure of performance of the test'
    print '%s\n' % ('=' * 25)


if __name__ == '__main__':
    main()
    caption()
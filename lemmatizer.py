#!/usr/bin/env python3
"""
Usage:
lemmatizer.py <infile> <outfile>
"""

import argparse

from estnltk import Text

def lemmatize(text: Text):
    text = Text(text)
    text.tag_layer(['words', 'morph_analysis'])
    return text.words

def returnparser():
    parser = argparse.ArgumentParser(
        description='Lemmatize infile text to outfile')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    return parser


def main(p: argparse.ArgumentParser):
    args = p.parse_args()


if __name__ == '__main__':
    argparser = returnparser()
    main(argparser)
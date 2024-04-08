#!/usr/bin/env python3
"""
Usage:
lemmatizer.py <infile> <outfile>
"""

import argparse

from estnltk import Text

def variants(sisu: list) -> list:
    out = list(set(sisu))
    return ['|'.join(out)]

def lemmatize(text: Text):
    text = Text(text)
    text.tag_layer(['words', 'morph_analysis'])
    lemmas = [list(x.lemma) for x in list(text.words)]
    lemmas = [variants(x) for x in lemmas]
    return lemmas

def returnparser():
    parser = argparse.ArgumentParser(
        description='Lemmatize infile text to outfile')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    return parser


def main(p: argparse.ArgumentParser):
    args = p.parse_args()
    with open(args.infile, 'r') as f:
        sisu = f.read()
    print(sisu)
    lemlist = lemmatize(sisu)
    print(' '.join([x[0] for x in lemlist]))
    print(len(lemlist))


if __name__ == '__main__':
    argparser = returnparser()
    main(argparser)
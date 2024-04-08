#!/usr/bin/env python3
"""
Teeb sisendfailist väljundfaili, kus iga sõna on asendatud lemmaga.

Lemmatiseerija ei tee mingit ühestamist, kui lemma on mitmene, siis
jätakse kõik variandid sisse, eraldatakse püstkriipsuga (`|`).

Eeldab installeeritud ja töötavat `estnltk` moodulit (https://estnltk.github.io/).

Kasutus:
./lemmatizer.py <infile> <outfile>

Usage:
lemmatizer.py <infile> <outfile>
"""

import argparse

from estnltk import Text

def variants(sisu: list) -> list:
    out = list(set(sisu))
    return ['|'.join(out)]

def lemmatize(text: Text) -> list:
    """

    :param text: Sisendtekst estnltk Text väärtusena
    :return: list, mille iga liige on string, mis sisaldab parjasti
    ühe lemma või mitu lemmat, mis on omavahel eraldatud püstkriipsuga (|)
    """
    text = Text(text)
    text.tag_layer(['words', 'morph_analysis'])
    lemmas = [list(x.lemma) for x in list(text.words)]
    lemmas = [variants(x)[0] for x in lemmas]
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
    out = ' '.join(lemlist)
    with open(args.outfile, 'w') as of:
        of.write(out)


if __name__ == '__main__':
    argparser = returnparser()
    main(argparser)
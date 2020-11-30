#!/usr/bin/env python3

from gensim.models import Word2Vec

model = Word2Vec.load('ja/ja.tsv')

print(model.wv.most_similar('講義'))

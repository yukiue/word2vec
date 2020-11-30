#!/usr/bin/env python3

from gensim.models import Word2Vec

model = Word2Vec.load('./models/ja.bin')

print(model.wv.most_similar('私'))

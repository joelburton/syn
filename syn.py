"""Synonym guessing game, useful for speech therapy."""

import random
import requests

words = open("syn.txt").readlines()
API = "https://api.datamuse.com/words?ml="

while True:
    word = random.choice(words)
    data = requests.get(API + word).json()
    syns =[
        d['word']
        for d in data
        if 'syn' in d.get('tags', [])
        and ' ' not in d['word']
        and d['score'] > 60000]

    # not enough synonyms
    if len(syns) < 7:
        continue

    print("\n\n" + word)
    input("Provide synonyms> ")
    for w in syns:
        print(w)

#!/usr/bin/env python
import json
import random

def lambda_handler(event=None, context=None):
    count = 30
    proverb = []

    with open("moody-album-dict.json", "r") as f:
        pv = json.loads(f.read())

    w = random.choice(list(pv.keys()))
    proverb.append(w)
    for i in range(count):
        try:
            w = random.choice(pv[w])
        except IndexError:
            break
        proverb.append(w)

    return {"moody album title": " ".join(proverb)}

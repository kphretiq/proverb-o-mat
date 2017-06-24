#!/usr/bin/env python
import json
import random

def lambda_handler(event=None, context=None):
    with open("moody-album-dict.json", "r") as f:
        pv = json.loads(f.read())

    return {
            "band name": artsy(pv),
            "title": artsy(pv),
            "tracks": [artsy(pv) for i in range(6)]
            }

def artsy(pv):
    count = 30
    proverb = []
    w = random.choice(list(pv.keys()))
    proverb.append(w)
    for i in range(count):
        try:
            w = random.choice(pv[w])
        except IndexError:
            break
        proverb.append(w)

    return " ".join(proverb)

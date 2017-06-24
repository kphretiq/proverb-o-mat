#!/usr/bin/env python

import json

with open("proverbs.json", "r") as p:
    proverbs = json.loads(p.read())
    proverbs_dict = {}
    with open("proverb-dict.json", "w") as pd:
        for k in proverbs:
            if not k == "":
                if not proverbs[k] == []:
                    proverbs_dict[k] = proverbs[k]
        pd.write(json.dumps(proverbs_dict, indent=True))
        

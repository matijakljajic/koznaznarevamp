# -*- coding: utf-8 -*-
"""

Q&A generator using Pandas and Random.

"""

import pandas
import random

qna = pandas.read_excel("izvucena_pitanja.xlsx", "sheet", usecols = "A,B")
qnad = qna.to_dict('index')

while True:
    r = random.randint(0, len(qnad))
    print(qnad[r]["ПИТАЊЕ"])

    a = input()
    if(a == ""):
        print(qnad[r]["ОДГОВОР"])
        
    print()
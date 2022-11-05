# -*- coding: utf-8 -*-
"""

Random Q&A generator using Pandas.

"""

import pandas

q = pandas.read_excel("izvucena_pitanja.xlsx", "sheet", None, None, None, "A")
a = pandas.read_excel("izvucena_pitanja.xlsx", "sheet", None, None, None, "B")

qna = {'Pitanje': q,
       'Odgovor': a
       }

df = pandas.DataFrame([qna], columns = ['Pitanje', 'Odgovor'])

p1 = q.sample()
p2 = a.sample()


print(p1)
print(p2)

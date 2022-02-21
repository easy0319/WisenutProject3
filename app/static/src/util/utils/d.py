from operator import index
import pandas as pd

df = pd.read_csv('user_dic.tsv')
a = []
a = df.values.tolist()

import numpy as np

b = np.array(a).flatten().tolist()
c = []
for i in b:
    c.append(i.split(' ')[0])

print(c)

ds = pd.DataFrame({1:c,2:'NNG'})

ds.to_csv('user_dic1.tsv', encoding='utf-8-sig', index=False, header=False, sep='\t')
import pandas as pd

df = pd.DataFrame(
    [
        [0, 0, 0, 1],       # 1
        [0, 0, 1, 1],       # 2
        [0, 1, 0, 1],       # 3
        [0, 1, 1, 1],       # 4
        [1, 0, 0, 0],       # 5
        [1, 0, 1, 1],       # 6
        [1, 1, 0, 1],       # 7
        [1, 1, 1, 1]        # 8
     ],
     columns = ["A", "B", "C", "(A~C)∨(A->B)"]
)

# таблица из исходной с результатом = 0
r = (df.loc[df['(A~C)∨(A->B)']==0, ['A','B','C']].astype(bool)).astype('int8')

# Находим СКНФ с помощью таблицы с результатом 0
res = (r.apply(lambda r: '({}{} ∨ {}{} ∨ {}{})'.format(
    '!'*r['A'], 'A', 
    '!'*r['B'], 'B', 
    '!'*r['C'], 'C' ), axis=1).str.cat(sep = ' ^ '))

print(df)

print(res)
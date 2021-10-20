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

# Инвертированная таблица с результатом = 1
r = (~df.loc[df['(A~C)∨(A->B)']==1, ['A','B','C']].astype(bool)).astype('int8')

# Находим СДНФ с помощью инвертированной таблицы
res = (r.apply(lambda r: '({}{} ^ {}{} ^ {}{})'.format(
    '!'*r['A'], 'A', 
    '!'*r['B'], 'B', 
    '!'*r['C'], 'C' ), axis=1).str.cat(sep = ' ∨ '))

print(df)

print(res)
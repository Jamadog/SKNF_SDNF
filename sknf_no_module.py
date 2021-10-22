funct = [
#    A  B  C  Res
    [0, 0, 0, 1], 
    [0, 0, 1, 1], 
    [0, 1, 0, 1], 
    [0, 1, 1, 1], 
    [1, 0, 0, 0], 
    [1, 0, 1, 1], 
    [1, 1, 0, 1], 
    [1, 1, 1, 1]  
]
res_ = []
for i in range(len(funct)):
    if funct[i][-1] == 0:
        res_.append(funct[i])

sknf = []
for i in range(len(res_)):
    x = []
    if res_[i][0] == 0:
        x.append('A')
    elif res_[i][0] == 1:
        x.append('!A')
    if res_[i][1] == 0:
        x.append('B')
    elif res_[i][1] == 1:
        x.append('!B')
    if res_[i][2] == 0:
        x.append('C')
    elif res_[i][2] == 1:
        x.append('!C')
    sknf.append(x)
    
# Вывод если 1 результат СКНФ
if (len(sknf) == 1):
    print("{} ∨ {} ∨ {}".format(sknf[0][0], sknf[0][1], sknf[0][2]))

# Вывод если более 1-го результата СКНФ
if (len(sknf) > 1):
    for i in range(len(sknf)):
        if i == len(sknf)-1:
            print(" ({} ∨ {} ∨ {})".format(sknf[i][0], sknf[i][1], sknf[i][2]), end='')
        if i != len(sknf)-1:
            print(" ({} ∨ {} ∨ {}) ".format(sknf[i][0], sknf[i][1], sknf[i][2]), end='&')
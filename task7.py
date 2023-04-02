stroka = input()

if 'f' not in stroka:
    pass
elif stroka.count('f') == 1:
    print(stroka.index('f'))
else:
    print(stroka.index('f'), stroka.rindex('f'))
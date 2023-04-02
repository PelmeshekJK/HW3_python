def task3(elem):
    last_elem = elem[-1]
    for i in range(len(elem)-1, 0, -1):
        elem[i] = a[i-1]
    elem[0] = last_elem
    return elem

a = []
for i in input().split():
    a.append( int(i) )
print(task3(a))

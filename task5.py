spisok = input().split()
equal = 0
for i in range(len(spisok)):
    for j in range(i+1, len(spisok)):
        if spisok[i] == spisok[j]:
            equal += 1
print(equal)
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

symmetric = True
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break

if symmetric:
    print("YES")
else:
    print("NO")
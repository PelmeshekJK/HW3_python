def can_eat(horse, other):
    x= abs(horse[0]-other[0])
    y= abs(horse[1]-other[1])
    return (x==1 and y==2) or (x==2 and y==1)

horse=tuple(map(int, input("введите расположение коня").split()))
other=tuple(map(int, input("введите расположение другой фигуры").split()))

print(can_eat(horse, other))

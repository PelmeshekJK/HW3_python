n = int(input("Количество дней: "))

kashi = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

for i in range(n):
    print(kashi[i%5])

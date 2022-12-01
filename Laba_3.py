# количество мальчиков и девочек одинаково. Сколько вариантов выбора есть?
n = int(input())
if n > 107 or n < 0:
    print("Out of range: n \n1<=x<=106")
    exit()

# делаем лист нулей
a = [0] * (n + 1)  # Девочки
b = [0] * n  # Мальчики
a[0] = 1
summa = 0
answer = 0

for ch in input():
    summa += [-1, +1][ch == 'a']  # Предыдущий и следующий элемент в листе
    if summa >= 0:
        answer += a[summa]
        a[summa] += 1
    else:
        answer += b[-summa]
        b[-summa] += 1
# print(sum([x*(x-1)//2 for x in a + b])) по сути тот же answer
print(answer)

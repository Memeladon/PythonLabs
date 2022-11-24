n = int(input())

family_tree = {}  # словарь {ребёнок=родитель}

# словарь family_tree
for _ in range(1, n):  # читаем строки
    line = input()
    child, parent = line.split()  # ребёнок,родитель = 'str1 str2'.split()
    family_tree[child] = parent  # family_tree[ребёнок]='родитель'

# все имена = все родители + все дети
all_man = set(family_tree.keys()) | set(family_tree.values())

levels = {}  # словарь {предок=поколение}


# вычисляет поколение, попутно создаёт словарь, чтоб не вычислять одно и тоже
def find_level(name):
    if name not in family_tree:  # если нет родителя
        levels[name] = 0  # предок = 0,запись в словарь levels
        return 0  # значение поколения для дальнейшего вычисления
    parent = family_tree[name]  # родитель = смотрим в (ребёнок=родитель)
    if parent in levels:  # если известно поколение родителя
        value = levels[parent] + 1  # поколение = (поколение родителя)+1
    else:
        value = find_level(
            parent) + 1  # поколение = поколение родителя +1, имя родителя отдаём функции, она вернёт поколение родителя
    levels[name] = value  # добавляем в словарь levels нового предка [имя] = поколение
    return value  # значение поколения для дальнейшего вычисления


# создадим словарь (предок=поколение)
for name in all_man:  # всех по очереди
    if name not in levels:  # берём только тех, кого нет в словаре (предок=поколение)
        find_level(name)

for name in sorted(levels):
    print(name, levels[name])

def MakeSet(x):
    parent[x] = x # элемент x является своим собственным представителем
    rank[x] = 0 # устанавливаем начальный ранг равным 0

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x]) # сжимаем путь
    return parent[x] # возвращаем корень множества для x

def Union(x, y):
    root_x = Find(x)
    root_y = Find(y)

    if root_x != root_y:
        # объединяем множества по рангам
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# вводим количество элементов
n = int(input("введите количество элементов: "))
parent = [0] * n # массив родительских элементов
rank = [0] * n # массив рангов

# создаем множество для каждого элемента
for i in range(n):
    MakeSet(i)

# бесконечный цикл для выполнения операций
while True:
    str_input = input("введите тип операции, где 1 - Find(x), 2 - Union(x, y), 0 чтобы завершить выполнение: ")

    if str_input == '2':  # проверяем, что это строка
        a = int(input('введите элемент x: '))
        b = int(input('введите элемент y: '))
        Union(a, b)
        print('parent =', parent)
        print('rank =', rank)

    elif str_input == '1':
        a = int(input('введите элемент x: '))
        print('корень его множества =', Find(a))

    elif str_input == '0':
        print('заканчиваем, пока!')
        break

    else:
        print("ошибка: введите правильное значение (1, 2 или 0)")
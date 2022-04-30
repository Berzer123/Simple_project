import math


def task_1():
    p = int(input())
    if p % 2 == 0 and p % 4 == 0:
        print('Yes')
    else:
        print('No')


def task_2():
    p = int(input())
    if p % 2 != 0 and p % 5 == 0:
        print('Yes')
    else:
        print('No')


def task_3():
    p = int(input())
    if p % 2 != 0 and p % 7 == 0:
        print('Yes')
    else:
        print('No')


def task_4():
    p = int(input())
    if p % 2 == 0 and p % 10 == 0:
        print('Yes')
    else:
        print('No')


def task_5():
    a, b, c, m, k = input(), input(), input(), input(), input()             # если а высота б ширина то с толщина, а <= m and b <= k
    if a <= m and b <= k:
        print('Yes')
    else:
        print('No')


def task_6():
    n = int(input())
    if n == 0:
        print('Ноль')
    elif n > 0:
        print('Положительное')
    else:
        print('Отрицательное')


def task_7():
    d = float(input())
    a = float(input())
    if math.sqrt(2) * a <= d:
        print('Yes')
    else:
        print('No')


def task_8():
    s = int(input())    # площадь сцены
    r = int(input())    # диаметр сцены
    k = int(input())    # проход
    if s - k > r:
        print('Yes')
    else:
        print('No')


def task_9():
    n = int(input('Макс мест 54 если что, угу-угу: '))
    if n > 36:
        print('Боковое')
    else:
        if n % 2 == 0:
            print('Верхний')
        elif n % 2 != 0:
            print('Нижний')
        else:
            print('Такого места нет')


def task_10():
    n = int(input())
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    while n > 499 and n > 0:
        n -= 500
        a1 += 1
    while n > 99 and n > 0:
        n -= 100
        a2 += 1
    while n > 9 and n > 0:
        n -= 10
        a3 += 1
    while n > 1 and n > 0:
        n -= 2
        a4 += 1
    if n == 0:
        print('Куп 500:' + str(a1), 'Куп 100:'+str(a2), 'Куп 10:'+ str(a3), 'монеты 2:'+ str(a4))
    else:
        print('Разменять нельзя')


def task_11():
    a = int(input('ребро куба:'))
    va = a * a * a # объём куба
    h = int(input('Высота цилиндра:'))
    r = int(input('Радиус цилндра:'))
    vr = math.pi * (r * r) * h  # объём цилиндра
    m = int(input('Объём жидкости:'))
    if va >= m:
        print('В куб поместится')
    if vr >= m:
        print('в цилиндр поместится')
    if va < m and vr < m:
        print('Никуда не поместится, увы...')


def task_12():
    a = int(input('ребро куба:'))
    va = a * a * a  # объём куба
    print('Объём куба', va)
    h = int(input('Высота цилиндра:'))
    r = int(input('Радиус цилндра:'))
    vr = math.pi * (r * r) * h  # объём цилиндра
    print('Объём цилиндра',vr)
    m = int(input('Объём жидкости:'))
    count = 0
    if va + vr <= m:
        print('Заполнится обе')
    elif va <= m:
        print('Заполнится первая')
    elif vr <= m:
        print('Заполнится вторая')
    else:
        print('Ничего не заполнится')


task_12()
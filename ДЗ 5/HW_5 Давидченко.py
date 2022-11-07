import re
import sys
import timeit
import random as rd


def polish_rec(in_str: str) -> str:
    """
    функція здійснює перетворення вхідної строки in_str, яка містить класичний запис
    арифметичних операції, в постфіксиний спосіб запису такої строки.
    Отримана постфіксна строка передається функції decide_polish,
    яка і здійснює безпосередньо  обрахунок арифметичних операції.
    Тести показали, що слабкім місцем у часу виконанні є запис та читання з файлу.
    В одному випадку без використання eval код виконується швидче, в іншому - ні.
    Важливо!!! проблема унарного "мінуса" не вирішувалась.

    :param in_str: вхідна строка з записом аріфмитичних операції
    :return: результат виконання арифметичних операції типу  str
    """
    # визначаємо словник із пріоритетом арифметичних операцій
    dict_pr = {'(': 0, ')': None, '+': 2, '-': 2, '*': 3, '%': 3, '/': 3, }
    # оголошуємо стек для зберігання операцій
    stack = []
    # оголошуємо список, який буде містити кінцевий результат
    out_str = []

    # створюємо регулярний вираз для роботи з елементами строки.
    # елементами регулярного виразу є: числа, дужки та операції
    for match in re.finditer('\d+|[+-/*///%/(/)]', in_str):
        sym = match.group(0)

        # реалізація алгоритму перетворення у постфіксну строку.
        # при визначення приорітетності операції використувується словник
        if sym == ' ':
            pass
        elif sym.isdigit():
            out_str.append(sym)
        elif sym == '(':
            stack.append(sym)
        elif sym == ')':
            out_symb = ')'
            while out_symb != '(':
                out_symb = stack.pop()
                if out_symb != '(':
                    out_str.append(out_symb)
        elif sym in '+-*/%':
            while len(stack) and dict_pr[stack[len(stack) - 1]] >= dict_pr[sym]:
                out_str.append(stack.pop())
            stack.append(sym)
    while len(stack):
        out_str.append(stack.pop())

    return decide_polish(out_str)


def decide_polish(postfix_str) -> str:
    """
    фунція здійснює арифметичні операції зі строкою у постфіксному форматі
    :param postfix_str: строку у постіфіксному форматі
    :return: результат виконання аріфметичих операції у форматі str
    """
    # словник визначає функції, які відповідають кожній  операції

    operator = {'+': lambda p1, p2: p1 + p2,
                '*': lambda p1, p2: p1 * p2,
                '-': lambda p1, p2: p1 - p2,
                '%': lambda p1, p2: None if not p2 else p1 % p2,
                '/': lambda p1, p2: None if not p2 else p1 / p2
                }

    # оголошуємо стек для виконання операції
    stack = []
    # реалізація алгоритму обрахунку постфіксної строки
    for i in postfix_str:
        if i.isdigit():
            stack.append(int(i))
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            res = operator[i](p2, p1)
            if res is None:
                return "division by zero"
            stack.append(res)

    return str(stack.pop())


def use_eval(in_str):
    """
    функція здійснює обрахування вхідної арифметичної строки in_str з використанням
    фунції eval.
    :param in_str: вхідна строка, яка містить аріфметичний вираз
    :return: результат обчислення, або повідомлення про 'division by zero'
    """

    try:
        return str(eval(in_str))
    except ZeroDivisionError:
        return 'division by zero'


def task_2(used_eval=False):
    """ Summary
    виконання завдання 5_2. Функція  eval для слабаків, тому пішов іншим шляхом.
    Ще зі шкільних часів пам'ятаю про постфіксний варіант запису математичних виразів.
    Це і використаю. Також, хочеться поексперементувати з функціями, передачею їх
    як параметрів.
    :param used_eval - визначає спосіб виконання завдання 2. Якщо eval == True,
    то відбувається використання функції eval(), у протилежному випадку - ні.



    """

    with open('file_1.txt') as f:
        lines = [line.replace('\n', '').replace(' ', '') for line in f]
        # print(lines)
        f.close()

    if not used_eval:
        lines = [lines[i] + '=' + polish_rec(line) + '\n' for i, line in enumerate(lines)]

    else:
        lines = [lines[i] + '=' + use_eval(line) + '\n' for i, line in enumerate(lines)]

    with open('file_1.txt', 'w') as f:
        f.writelines(lines)
        f.close()


def full_task_2():
    """
    функція виконує завдання 2 двома підходами із  з визначенням часу виконання
    кожного з них.

    :return: нічого не повертає
    """
    task_2(used_eval=False)
    task_2(used_eval=True)

    print('час виконання без використання eval:')
    print(timeit.timeit("task_2(used_eval=False)", setup="from __main__ import task_2", number=100))

    print('час виконання з  використанням eval:')
    print(timeit.timeit("task_2(used_eval=True)", setup="from __main__ import task_2", number=100))


def index_sort(list_loc, begin, end, reverse=False):
    """
    функція здійснює сортування елементів міє індексами begin та end.
    елементи з індексами begin та end не включається у діапазон сортування
    :param list_loc: вхідний список
    :param begin: індекс елементу початку сортування (не включно)
    :param end:  індекс елементу закінчення сортування (не включно)
    :param reverse: напрямок сортування
    :return: повертає список з відсортованим зрізом
    """

    if end > begin and begin >= 0:
        list_loc[begin + 1:end] = sorted(list_loc[begin + 1:end], reverse=reverse)
        return list_loc
    else:
        print('помилка інтервалу сортування')
        sys.exit()


def task_1():
    """ Зміст завдання:
    1. Створіть функцію, яка приймає список, та індекс
	початку сортування та індекс кінця сортування,
	і повертає список у якому відсортовані лише ті елементи,
	які укладені між індексом початку сортування та індексом
	кінця сортування.
		Наприклад:
			[1,10,9,4,5,7,2,0], 2, 6
		Відповідь
			[1,10,4,5,7,9,2,0]

	У відповіді повернути ПОЧАТОКОВИЙ список але з
	відсортованою частиною!
    """

    # математичне очікування для генерації списку
    mu = 0
    # середньо-квадратичне відхилення для генерації списку
    sigma = 55
    # кількість елементів у списку
    num = 15
    # генерація списку
    list_loc = [round(rd.gauss(mu, sigma), 2) for i in range(num)]
    print('згенерований список', list_loc)
    list_loc = index_sort(list_loc, 0, 3)
    print('відсортовний список', list_loc)


def clear_line(in_line):
    """
    функція здійснює очистку строки від символів, які не є літерами, та переводить усі
    символи в нижній регістр
    :param in_line: вхідна строка
    :return: строка після обробки
    """
    # створюємо дублікат строки для виконання очистки
    res_line = in_line
    # цікл обходить кожний символ та якщо він не є символом, то видаляє усі такі символи із строки
    for sym in in_line:
        if not sym.isalpha():
            res_line = res_line.replace(sym, '')
    res_line = res_line.lower()
    return res_line


def task_3():
    """
    функція виконує завдання 3 "поліндром".
    Поліндроми знаходятья у файлі polyndrom.txt

    :return:
    """

    with open('polyndrom.txt') as f:
        # список source_line містить вхідні строки, які не змінювались.
        # Неообхідно для виведення результату
        source_line = [line.replace('\n', '') for line in f]
        # lines - список, що містить "очищені строки". Таку очистку здійснює функція clear_line()
        lines = [clear_line(line) for line in source_line]
        f.close()

    for i, line in enumerate(lines):
        print('строка "{0}" поліндром'.format(source_line[i])) if (
            lambda line: True if line == line[::-1] else False) else print(
            'строка "{0}" не поліндром'.format(source_line[i]))


if __name__ == '__main__':
    full_task_2()
    task_1()
    task_3()

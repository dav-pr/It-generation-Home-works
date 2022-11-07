import random
import string


# початок коду до завдання 1
def midle(s):
    # функція виводить на екран символ або символи, які знаходяться в середині рядка
    if len(s) % 2:
        res = s[len(s) // 2]
    else:
        index = len(s) // 2 - 1
        res = s[index:index + 2]

    print('символ(и) у середені строки - {0}'.format(res), )
    return res


def task_1():
    # функція безпосерденьо виконує завдання 1

    print('\n', "*" * 20, "завдання 1", "*" * 20, '\n')
    all_middle_sym = ''

    for i in range(3):
        all_middle_sym += midle(input('введіть строку № {0} \n'.format(i)))

    print('усі середні символи трьох строк - "{0}"'.format(all_middle_sym), )


# завершення коду до завдання 1


# початок коду до завдання 2

def generate_str(length):
    # функція генерує випадкову строку завданої довжини
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def get_half(s):
    # функція ділить строку s на дві частини
    # s - строка
    # функція повертає дві частини та центральний символ у випадку непарної довжини строки
    # one_half - перша половина строки
    # one_half друга половина строки
    # center_symbol - центральний символ

    if len(s) % 2:
        one_half = s[0:len(s) // 2]
        two_half = s[len(s) // 2 + 1:]
        center_symbol = s[len(s) // 2]
    else:
        one_half = s[0:len(s) // 2]
        two_half = s[len(s) // 2:]
        center_symbol = ''

    return one_half, two_half, center_symbol


def task_2():
    # функція безпосерденьо виконує завдання 2
    print('\n', "*" * 20, "завдання 2", "*" * 20, '\n')
    str_gen = generate_str(random.randint(5, 15))
    one_half, two_half, center_symbol = get_half(str_gen)

    print('згенерована строка - ', str_gen)
    print('перша частина - ', one_half)
    print('друга частина - ', two_half)
    print('центральний символ - ', center_symbol if center_symbol else 'відсутній')

    two_half = two_half[0:len(two_half) - 3] + two_half[len(two_half) - 3:len(two_half)].upper()
    print('перетворена друга частина - ', two_half)
    str_gen = two_half + center_symbol + one_half
    print('перетворена строка - ', str_gen)


# завершення коду до завдання 2

# початок коду до завдання 3
def task_3():
    # функція безпосерденьо виконує завдання 3
    print('\n', "*" * 20, "завдання 3", "*" * 20, '\n')

    # генеремо строку довжиною від 5 до 10 включно. Мінімальна довжина пов'язана з умовами задачі.
    str_gen = generate_str(random.randint(5, 10))
    print('згенерована строка - ', str_gen)
    # отримуємо останні 3 символи
    last_3 = str_gen[len(str_gen) - 3:len(str_gen)].lower()
    # отримуємо подстроку з виключенням останнім 3-х символов
    str_gen = str_gen[0:len(str_gen) - 3]
    print('згенерована  обрізана строка ', str_gen)
    print('останні три символи ', last_3)
    # розділяємо строку на дві частини
    one_half, two_half, center_symbol = get_half(str_gen)
    # оскільки умовами задачі не описано, як потрібно діяти, коли залишок строки має непарну
    # довжину, то середній символ викідається
    print ('центральний виброшений символ - ', center_symbol ) if center_symbol else print ('відсутній')
    str_gen = one_half + last_3 + two_half
    print('перетворена строка - ', str_gen)


# початок коду до завдання 4
def input_num(name):
    # функція здійснює контроль правильності введення даних
    try:
        num = int(input('Введіть натуральне число ' + name + ' '))
        if num <= 0:
            raise Exception("Число мaє бути більше 0")

        return num
    except:
        print('Має бути введено ціле число. Спробуйте ще раз')
        input_num(name)


def print_line(size, fill=' ', new_line=True):
    # функція виводить та екран одну лінію
    # fill - заповнюч середини квадрата, для першої і останньої лінії від буде "#"
    # new_line - ознака необхідності перейти на нову строку перед початком виводу строки

    if new_line:
        print('')
    print('#', end='')
    for i in range(size - 2):
        print(fill, end='')
    # здійснюємо перевірку ситуації, коли розмір квадрату = 1,
    # у такому випадку не потрібно виводити "останній" символ строки, він вже виведений
    if size > 1:
        print('#', end='')


def task_4():
    # функція безпосерденьо виконує завдання 4

    print('\n', "*" * 20, "завдання 4", "*" * 20, '\n')
    n = input_num(' розмір квадрату ')
    for i in range(n):
        # виводимо першу строку квадрата
        if i == 0:
            print_line(n, fill="#")
        # виводемо останню строку квадрата
        elif i == n - 1:
            print_line(n, fill="#")
        # виводемо строки, крім першої і останньої
        else:
            print_line(n)


# завершення коду до завдання 4

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()

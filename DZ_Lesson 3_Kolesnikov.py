#1. Реализовать функцию, принимающую два числа
#(позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя,
#предусмотреть обработку ситуации деления на ноль.

#def main(a, b):
#    try:
#        return a / b
#    except ZeroDivisionError:
#        return "Ошибка деления"

#x = int(input("Введите число x >>> "))
#y = int(input("Введите число y >>> "))

#print(main(x, y))


#2. Реализовать функцию, принимающую несколько параметров,
#описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать
#параметры как именованные аргументы. Реализовать вывод данных
#о пользователе одной строкой.

#def main(**kwargs):
#     return f"{kwargs['first_name']} {kwargs['last_name']} ({kwargs['year']}), {kwargs['city']}, {kwargs['phone']}, {kwargs['email']}"


#user_first_name = input("Имя >>> ")
#user_last_name = input("Фамилия >>> ")
#user_year = int(input("Год рождения >>> "))
#user_city = input("Город >>> ")
#user_email = input("Email >>> ")
#user_phone = input("Номер телефона >>> ")

#print(
#    main(first_name=user_first_name, last_name=user_last_name,
#         year=user_year, city=user_city, email=user_email,
#         phone=user_phone)
#)

#3. Реализовать функцию my_func(), которая принимает три позиционных
#аргумента, и возвращает сумму наибольших двух аргументов.

#def my_func(arg1 , arg2, arg3):
#    if arg1 >= arg3 and arg2 >= arg3:
#        return arg1 + arg2
#    elif arg1 > arg2 and arg1 < arg3:
#        return arg1 + arg3
#    else:
#        return arg2 + arg3

#print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')

#4. Программа принимает действительное положительное число x
#и целое отрицательное число y. Необходимо выполнить возведение
#числа x в степень y. Задание необходимо реализовать в виде функции
#my_func(x, y). При решении задания необходимо обойтись без встроенной
#функции возведения числа в степень

#def my_func(x, y):
#    return x ** y
#a, b = float(input("Число a >>> ")), int(input("Число b >>> "))
#print(my_func(a, b))

#5. Программа запрашивает у пользователя строку чисел, разделенных
#пробелом. При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и
#снова нажать Enter. Сумма вновь введенных чисел будет добавляться
#к уже подсчитанной сумме. Но если вместо числа вводится специальный
#символ, выполнение программы завершается. Если специальный символ
#введен после нескольких чисел, то вначале нужно добавить сумму этих
#чисел к полученной ранее сумме и после этого завершить программу.

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Финальная сумма {sum_res}')

my_sum()

#Реализовать функцию int_func(), принимающую слово из маленьких
#латинских букв и возвращающую его же, но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать
#строка из слов, разделенных пробелом. Каждое слово состоит
#из латинских букв в нижнем регистре. Сделать вывод исходной
#строки, но каждое слово должно начинаться с заглавной буквы.
#Необходимо использовать написанную ранее функцию int_func().

#def int_func (*args):
#    word = input("Input words ")
#    print(word.title())
#    return
#int_func()
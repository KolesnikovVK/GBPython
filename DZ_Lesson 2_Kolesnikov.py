# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

#list = ["Привет", 1, 3.8, True, [], {}, None]

#for item in list:
#    print(type(item))

#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# ля заполнения списка элементов необходимо использовать функцию input().


#elements = input("Укажите значения списка через запятую >>> ").split(",")

#max_idx = len(elements) - 1

#for idx in range(0, max_idx, 2):
#    next_idx = idx + 1
#    elements[idx], elements[next_idx] = elements[next_idx], elements[idx]

#print(elements)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#month = int(input("Номер месяца >>> "))

#year = {
#    "зима": (12, 1, 2),
#    "весна": (3, 4, 5),
#    "лето": (6, 7, 8),
#    "осень": (9, 10, 11),
#}

#for season, months in year.items():
#    if month in months:
#        print(f"Время года = {season}")
#        break

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

#string = input("Введите строку >>> ")
#word = []
#num = 1
#for el in range(string.count(' ') + 1):
#    word = string.split()
#    if len(str(word)) <= 10:
#        print(f" {num} {word [el]}")
#        num += 1
#    else:
#        print(f" {num} {word [el] [0:10]}")
#        num += 1


#Реализовать структуру «Рейтинг», представляющую собой
#не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться
#после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде,
#например, my_list = [7, 5, 3, 3, 2].

list = [6, 7, 4, 1, 5, 5, 3, 6, 7]
print(f"Рейтинг - {list}")
digit = int(input("Введите число >>> (10 - выход) "))
while digit != 10:
    for el in range(len(list)):
        if list[el] == digit:
            list.insert(el + 1, digit)
            break
        elif list[0] < digit:
             list.insert(0, digit)
        elif list[-1] > digit:
             list.append(digit)
        elif list[el] > digit and list[el + 1] < digit:
             list.insert(el + 1, digit)
    print(f"текущий список - {list}")
    digit = int(input("Введите число "))
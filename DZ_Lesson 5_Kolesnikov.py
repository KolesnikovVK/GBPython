#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. #Об окончании ввода данных свидетельствует пустая строка.

#my_file = open('test.txt', 'w')
#line = input('Введите текст \n')
#while line:
#    my_file.writelines(line)
#    line = input('Введите текст \n')
#    if not line:
#        break

#my_file.close()
#my_file = open('test.txt', 'r')
#content = my_file.readlines()
#print(content)
#my_file.close()

#2. Создать текстовый файл (не программно), сохранить в нем
#несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


#my_file = open('test.txt', 'r')
#content = my_file.read()
#print(f'Содержимое файла: \n {content}')
#y_file = open('test.txt', 'r')
#content = my_file.readlines()
#print(f'Количество строк в файле - {len(content)}')
#my_file = open('test.txt', 'r')
#content = my_file.readlines()
#for i in range(len(content)):
#    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
#my_file = open('test.txt', 'r')
#content = my_file.read()
#content = content.split()
#print(f'Общее количество слов - {len(content)}')
#my_file.close()

#3.Создать текстовый файл (не программно), построчно записать
#фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней
#величины дохода сотрудников.

#with open('test.txt', 'r') as my_file:
#    salary = []
#    poor = []
#    my_list = my_file.read().split('\n')
#    for i in my_list:
#        i = i.split()
#        if int(i[1]) < 20_000:
#           poor.append(i[0])
#        salary.append(i[1])
#print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, salary)) / len(salary)}')

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение
#и считывающую построчно данные. При этом английские
#числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.


#my_file = open('test1.txt', 'w')
#rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
#new_file = []
#with open('test1.txt', 'r') as file_obj:
    #content = file_obj.read().split('\n')
#    for i in file_obj:
#        i = i.split(' ', 1)
#        new_file.append(rus[i[0]] + '  ' + i[1])
#    print(new_file)

#with open('test1_new.txt', 'w') as file_obj_2:
#    file_obj_2.writelines(new_file)

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

#def summary():
#    try:
#        with open('file_5.txt', 'w+') as file_obj:
#            line = input('Введите цифры через пробел \n')
 #           file_obj.writelines(line)
#            my_numb = line.split()

#            print(sum(map(int, my_numb)))
#    except IOError:
#        print('Ошибка в файле')
#    except ValueError:
#        print('Неправильно набран номер. Ошибка ввода-вывода')
#summary()

#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
#наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
#Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#Вывести словарь на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

#my_file = open('test1.txt', 'w')
#subj = {}
#with open('test1.txt', 'r') as init_f:
#    for line in init_f:
#        subject, lecture, practice, lab = line.split()
#        subj[subject] = int(lecture) + int(practice) + int(lab)
#    print(f'Общее количество часов по предмету - \n {subj}')

#7. Создать вручную и заполнить несколькими строками текстовый файл,
#в котором каждая строка должна содержать данные о фирме: название,
#форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

import json

companies_data = []

with open('task.txt') as input_data:
    companies_dict = {}
    profit_list = []

    for company_row in input_data:
        name, form, revenue, costs = company_row.split()

        profit = float(revenue) - float(costs)
        companies_dict[name] = profit

        if profit:
            profit_list.append(profit)

    companies_data.append(companies_dict)
    companies_data.append({
        "average_profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open('task.json', 'w') as output_data:
    json.dump(companies_data, output_data)

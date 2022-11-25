#import Levenshtein
#import pandas as pd
#import os

import io
import csv
import colorama

colorama.init()

#Просмотр всей базы данных
def ShowAllDatabase():

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        LineCounter = 0
        for row in file_reader:
            print(f'{LineCounter} ::: {row}')
            LineCounter += 1

#Просмотр базы данных по источнику
def ShowDatabaseBySource():

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)

        AllSourceList = []

        for row in file_reader:
            if row[5] not in AllSourceList:
                AllSourceList.append(row[5])

        print('Список источников:')
        for i in range(0, len(AllSourceList)):
            print(f'{i+1} - {AllSourceList[i]}')

        SourceNum = int(input('Введите номер источника: ')) - 1

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)

        LineCounter = 0
        for row in file_reader:
            if row[5] == AllSourceList[SourceNum]:
                print(f'{LineCounter} ::: {row}')

#Поиск совпадений по всем источникам
def SearchAllDatabase():

    SearchTag = str(input('Введите тег для поиска: '))

    print('Выборка совпадений из базы данных: ')
    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in file_reader:
            if SearchTag in str(row):
                print(row)

    SearchTechnologyList = []
    SearchDomainList = []
    SearchFuncList = []
    SearchAtributeList = []
    SearchScientistList = []
    SearchSourceList = []
    SearchConnectTechnologiesList = []

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in file_reader:
            if SearchTag in str(row):
                TechnologyList = row[0].split(';')
                DomainList = row[1].split(';')
                FuncList = row[2].split(';')
                AtributeList = row[3].split(';')
                ScientistList = row[4].split(';')
                SourceList = row[5].split(';')
                ConnectTechnologiesList = row[6].split(';')

                for i in range(0, len(TechnologyList)):
                    if TechnologyList[i] not in SearchTechnologyList:
                        SearchTechnologyList.append(TechnologyList[i])
                for i in range(0, len(DomainList)):
                    if DomainList[i] not in SearchDomainList:
                        SearchDomainList.append(DomainList[i])
                for i in range(0, len(FuncList)):
                    if FuncList[i] not in SearchFuncList:
                        SearchFuncList.append(FuncList[i])
                for i in range(0, len(AtributeList)):
                    if AtributeList[i] not in SearchAtributeList:
                        SearchAtributeList.append(AtributeList[i])
                for i in range(0, len(ScientistList)):
                    if ScientistList not in SearchScientistList:
                        SearchScientistList.append(ScientistList[i])
                for i in range(0, len(SourceList)):
                    if SourceList[i] not in SearchSourceList:
                        SearchSourceList.append(SourceList[i])
                for i in range(0, len(ConnectTechnologiesList)):
                    if ConnectTechnologiesList[i] not in SearchConnectTechnologiesList:
                        SearchConnectTechnologiesList.append(ConnectTechnologiesList[i])

    while True:

        print('1 - Вывести список технологий')
        print('2 - Вывести список доменов')
        print('3 - Вывести список функций')
        print('4 - Вывести список атрибутов')
        print('5 - Вывести список ученых')
        print('6 - Вывести список источников')
        print('7 - Вывести список связанных технологий')
        print('8 - Выгрузить результаты в файл')
        print('0 - Вернуться в главное меню')

        SearchCounter = int(input('Введите номер пункта: '))

        if SearchCounter == 1:
            print('Технологии:')
            for i in range(0, len(SearchTechnologyList)):
                print(SearchTechnologyList[i])
        elif SearchCounter == 2:
            print('Домены:')
            for i in range(0, len(SearchDomainList)):
                print(SearchDomainList[i])
        elif SearchCounter == 3:
            print('Функции')
            for i in range(0, len(SearchFuncList)):
                print(SearchFuncList[i])
        elif SearchCounter == 4:
            print('Атрибуты:')
            for i in range(0, len(SearchAtributeList)):
                print(SearchAtributeList[i])
        elif SearchCounter == 5:
            print('Ученые:')
            for i in range(0, len(SearchScientistList)):
                print(SearchScientistList[i])
        elif SearchCounter == 6:
            print('Источники:')
            for i in range(0, len(SearchSourceList)):
                print(SearchSourceList[i])
        elif SearchCounter == 7:
            print('Связанные технологии:')
            for i in range(0, len(SearchConnectTechnologiesList)):
                print(SearchConnectTechnologiesList[i])
        elif SearchCounter == 8:
            OutCounterList = []
            OutList = []
            OutCounterList.append(int(input('Записывать технологии? (1/0): ')))
            OutCounterList.append(int(input('Записывать домены? (1/0): ')))
            OutCounterList.append(int(input('Записывать функции? (1/0): ')))
            OutCounterList.append(int(input('Записывать атрибуты? (1/0): ')))
            OutCounterList.append(int(input('Записывать ученых? (1/0): ')))
            OutCounterList.append(int(input('Записывать источники? (1/0): ')))
            OutCounterList.append(int(input('Записывать связанные технологии? (1/0): ')))
            if OutCounterList[0] == 1:
                OutList = OutList + SearchTechnologyList
            if OutCounterList[1] == 1:
                OutList = OutList + SearchDomainList
            if OutCounterList[2] == 1:
                OutList = OutList + SearchFuncList
            if OutCounterList[3] == 1:
                OutList = OutList + SearchAtributeList
            if OutCounterList[4] == 1:
                OutList = OutList + SearchScientistList
            if OutCounterList[5] == 1:
                OutList = OutList + SearchSourceList
            if OutCounterList[6] == 1:
                OutList = OutList + SearchConnectTechnologiesList

            WritingListToFile(OutList)

        elif SearchCounter == 0:
            break
        else:
            print('Пожалуйста, проверьте корректность ввода')

#Поиск совпадений по конкретному источнику
def SearchBySource():

    SearchTag = str(input('Введите тег для поиска: '))

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)

        AllSourceList = []

        for row in file_reader:
            if row[5] not in AllSourceList and SearchTag in str(row):
                AllSourceList.append(row[5])

        print('Список источников:')
        for i in range(0, len(AllSourceList)):
            print(f'{i+1} - {AllSourceList[i]}')

        SourceNum = int(input('Введите номер источника: ')) - 1

    print('Выборка совпадений из базы данных: ')
    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in file_reader:
            if row[5] == AllSourceList[SourceNum] and SearchTag in str(row):
                print(row)

    SearchTechnologyList = []
    SearchDomainList = []
    SearchFuncList = []
    SearchAtributeList = []
    SearchScientistList = []
    SearchSourceList = []
    SearchConnectTechnologiesList = []

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in file_reader:
            if row[5] == AllSourceList[SourceNum] and SearchTag in str(row):
                TechnologyList = row[0].split(';')
                DomainList = row[1].split(';')
                FuncList = row[2].split(';')
                AtributeList = row[3].split(';')
                ScientistList = row[4].split(';')
                SourceList = row[5].split(';')
                ConnectTechnologiesList = row[6].split(';')

                for i in range(0, len(TechnologyList)):
                    if TechnologyList[i] not in SearchTechnologyList:
                        SearchTechnologyList.append(TechnologyList[i])
                for i in range(0, len(DomainList)):
                    if DomainList[i] not in SearchDomainList:
                        SearchDomainList.append(DomainList[i])
                for i in range(0, len(FuncList)):
                    if FuncList[i] not in SearchFuncList:
                        SearchFuncList.append(FuncList[i])
                for i in range(0, len(AtributeList)):
                    if AtributeList[i] not in SearchAtributeList:
                        SearchAtributeList.append(AtributeList[i])
                for i in range(0, len(ScientistList)):
                    if ScientistList not in SearchScientistList:
                        SearchScientistList.append(ScientistList[i])
                for i in range(0, len(SourceList)):
                    if SourceList[i] not in SearchSourceList:
                        SearchSourceList.append(SourceList[i])
                for i in range(0, len(ConnectTechnologiesList)):
                    if ConnectTechnologiesList[i] not in SearchConnectTechnologiesList:
                        SearchConnectTechnologiesList.append(ConnectTechnologiesList[i])

    while True:

        print('1 - Вывести список технологий')
        print('2 - Вывести список доменов')
        print('3 - Вывести список функций')
        print('4 - Вывести список атрибутов')
        print('5 - Вывести список ученых')
        print('6 - Вывести список источников')
        print('7 - Вывести список связанных технологий')
        print('8 - Выгрузить результаты в текстовый файл')
        print('0 - Вернуться в главное меню')

        SearchCounter = int(input('Введите номер пункта: '))

        if SearchCounter == 1:
            print('Технологии:')
            for i in range(0, len(SearchTechnologyList)):
                print(SearchTechnologyList[i])
        elif SearchCounter == 2:
            print('Домены:')
            for i in range(0, len(SearchDomainList)):
                print(SearchDomainList[i])
        elif SearchCounter == 3:
            print('Функции:')
            for i in range(0, len(SearchFuncList)):
                print(SearchFuncList[i])
        elif SearchCounter == 4:
            print('Атрибуты:')
            for i in range(0, len(SearchAtributeList)):
                print(SearchAtributeList[i])
        elif SearchCounter == 5:
            print('Ученые:')
            for i in range(0, len(SearchScientistList)):
                print(SearchScientistList[i])
        elif SearchCounter == 6:
            print('Источники:')
            for i in range(0, len(SearchSourceList)):
                print(SearchSourceList[i])
        elif SearchCounter == 7:
            print('Связанные технологии:')
            for i in range(0, len(SearchConnectTechnologiesList)):
                print(SearchConnectTechnologiesList[i])
        elif SearchCounter == 8:

            OutCounterList = []
            OutList = []
            OutCounterList.append(int(input('Записывать технологии? (1/0): ')))
            OutCounterList.append(int(input('Записывать домены? (1/0): ')))
            OutCounterList.append(int(input('Записывать функции? (1/0): ')))
            OutCounterList.append(int(input('Записывать атрибуты? (1/0): ')))
            OutCounterList.append(int(input('Записывать ученых? (1/0): ')))
            OutCounterList.append(int(input('Записывать источники? (1/0): ')))
            OutCounterList.append(int(input('Записывать связанные технологии? (1/0): ')))
            if OutCounterList[0] == 1:
                OutList = OutList + SearchTechnologyList
            if OutCounterList[1] == 1:
                OutList = OutList + SearchDomainList
            if OutCounterList[2] == 1:
                OutList = OutList + SearchFuncList
            if OutCounterList[3] == 1:
                OutList = OutList + SearchAtributeList
            if OutCounterList[4] == 1:
                OutList = OutList + SearchScientistList
            if OutCounterList[5] == 1:
                OutList = OutList + SearchSourceList
            if OutCounterList[6] == 1:
                OutList = OutList + SearchConnectTechnologiesList

            WritingListToFile(OutList)

        elif SearchCounter == 0:
            break
        else:
            print('Пожалуйста, проверьте корректность ввода')

#Выгрузка результатов поиска в текстовый файл
def WritingListToFile(List):
    with open("result.txt", "w") as file:
        for line in List:
            file.write(line + '\n')

#Добавление записей в csv файл
def AddNewEntry():

    print('Добавление технологий в список ')
    print('Ввод нескольких Атрибутов в формате: Атрибут1;Атрибут2;АтрибутХ')

    AddList = []

    AddList.append(str(input('Введите название технологии: ')))
    AddList.append(str(input('Введите домены: ')))
    AddList.append(str(input('Введите функции: ')))
    AddList.append(str(input('Введите атрибуты: ')))
    AddList.append(str(input('Введите ученых: ')))
    AddList.append(str(input('Введите источники: ')))
    AddList.append(str(input('Введите связанные технологии: ')))

    print(AddList)

    with io.open('database.csv', mode= 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = '|', lineterminator="\r")
        file_writer.writerow(AddList)

#Поиск совпадение по csv файлу
def SearchForMatches():
    print('Поиск совпадений по тегу')
    while True:
        print('1 - Поиск совпадений по всем источникам')
        print('2 - Поиск совпадений по конкретному источнику')
        print('0 - Вернуться к выбору функций')

        SearchCounter = int(input('Введите цифорку: '))

        if SearchCounter == 1:
            SearchAllDatabase()
        elif SearchCounter == 2:
            SearchBySource()
        elif SearchCounter == 0:
            break
        else:
            print('Пожалуйста, проверьте корректность ввода')

#Показать содержимое базы данных
def ShowDatabase():
    print('Просмотр списка технологий')
    while True:
        print('1 - Просмотр всех технологий')
        print('2 - Просмотр технологий по источнику')
        print('0 - Вернуться к выбору функций')

        ShowCounter = int(input('Введите цифорку: '))

        if ShowCounter == 1:
            ShowAllDatabase()
        elif ShowCounter == 2:
            ShowDatabaseBySource()
        elif ShowCounter == 0:
            break
        else:
            print('Пожалуйста, проверьте корректность ввода')

#Внести изменения в существующую строку csv файла
def UpdateCsvRow():
    ShowAllDatabase()

    RowNumber = int(input('Введите номер строки: '))
    with io.open('database.csv', 'r', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        Lines = []
        AddList = []
        RowCounter = 0
        for row in file_reader:
            if RowCounter == RowNumber:
                AddList.append(str(input('Введите название технологии: ')))
                AddList.append(str(input('Введите домены: ')))
                AddList.append(str(input('Введите функции: ')))
                AddList.append(str(input('Введите атрибуты: ')))
                AddList.append(str(input('Введите ученых: ')))
                AddList.append(str(input('Введите источники: ')))
                AddList.append(str(input('Введите связанные технологии: ')))
                Lines.append(AddList)
            else:
                Lines.append(row)
            RowCounter += 1
    with io.open('database.csv', 'w', encoding='utf-8') as csv_file:
        csv.writer(csv_file, delimiter='|').writerows(Lines)

#Главная исполняемая функция
def main():
    print('Программа НИО МАИ 317 по поиску технологий')

    while True:
        print('1 - Найти совпадению по атрибутам')
        print('2 - Добавить новую запись')
        print('3 - Показать базу данных')
        print('4 - внести изменения в базу данных')
        print('0 - выйти из программы')

        FirstCounter = int(input('Введите цифорку: '))

        if FirstCounter == 1:
            SearchForMatches()
        elif FirstCounter == 2:
            AddNewEntry()
        elif FirstCounter == 3:
            ShowDatabase()
        elif FirstCounter == 4:
            UpdateCsvRow()
        elif FirstCounter == 0:
            break
        else:
            print('Пожалуйста, проверьте корректность ввода')

if __name__ == '__main__':
    main()

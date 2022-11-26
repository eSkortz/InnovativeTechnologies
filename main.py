#import Levenshtein
#import pandas as pd
#import os

import io
import csv
import colorama
from colorama import Fore, Back, Style

colorama.init()

#Просмотр всей базы данных
def ShowAllDatabase():

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        LineCounter = 0
        for row in file_reader:
            print(Fore.LIGHTWHITE_EX, f'{LineCounter} ::: {row}')
            LineCounter += 1

#Просмотр базы данных по источнику
def ShowDatabaseBySource():

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)

        AllSourceList = []

        for row in file_reader:
            if row[5] not in AllSourceList:
                AllSourceList.append(row[5])

        print(Fore.LIGHTWHITE_EX)
        print('Список источников:')
        for i in range(0, len(AllSourceList)):
            print(f'{i+1} - {AllSourceList[i]}')

        print(Fore.LIGHTGREEN_EX)
        SourceNum = int(input('Введите номер источника: ')) - 1

    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)

        LineCounter = 0
        for row in file_reader:
            if row[5] == AllSourceList[SourceNum]:
                print(Fore.LIGHTWHITE_EX, f'{LineCounter} ::: {row}')

#Поиск совпадений по всем источникам
def SearchAllDatabase():

    print(Fore.LIGHTGREEN_EX)
    SearchTag = str(input('Введите тег для поиска: '))

    print(Fore.LIGHTWHITE_EX, 'Выборка совпадений из базы данных: ')
    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        LineCounter = 0
        for row in file_reader:
            if SearchTag in str(row):
                print(f'{LineCounter} ::: {row}')
                LineCounter += 1

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
        print(Fore.LIGHTBLUE_EX)
        print('Вывести список технологий - 1')
        print('Вывести список доменов - 2')
        print('Вывести список функций - 3')
        print('Вывести список атрибутов - 4')
        print('Вывести список ученых - 5')
        print('Вывести список источников - 6')
        print('Вывести список связанных технологий - 7')
        print('Выгрузить результаты в текстовый файл - 8')
        print('Вернуться в главное меню - 0')

        print(Fore.LIGHTGREEN_EX)
        SearchCounter = int(input('Введите номер пункта: '))

        print(Fore.LIGHTWHITE_EX)
        if SearchCounter == 1:
            print('Технологии:')
            for i in range(0, len(SearchTechnologyList)):
                print(f'{i} ::: {SearchTechnologyList[i]}')
        elif SearchCounter == 2:
            print('Домены:')
            for i in range(0, len(SearchDomainList)):
                print(f'{i} ::: {SearchDomainList[i]}')
        elif SearchCounter == 3:
            print('Функции')
            for i in range(0, len(SearchFuncList)):
                print(f'{i} ::: {SearchFuncList[i]}')
        elif SearchCounter == 4:
            print('Атрибуты:')
            for i in range(0, len(SearchAtributeList)):
                print(f'{i} ::: {SearchAtributeList[i]}')
        elif SearchCounter == 5:
            print('Ученые:')
            for i in range(0, len(SearchScientistList)):
                print(f'{i} ::: {SearchScientistList[i]}')
        elif SearchCounter == 6:
            print('Источники:')
            for i in range(0, len(SearchSourceList)):
                print(f'{i} ::: {SearchSourceList[i]}')
        elif SearchCounter == 7:
            print('Связанные технологии:')
            for i in range(0, len(SearchConnectTechnologiesList)):
                print(f'{i} ::: {SearchConnectTechnologiesList[i]}')
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
            print(f'{AllSourceList[i]} - {i+1}')

        SourceNum = int(input('Введите номер источника: ')) - 1

    print('Выборка совпадений из базы данных: ')
    with io.open('database.csv', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter="|", quoting=csv.QUOTE_NONE)
        LineCounter = 0
        for row in file_reader:
            if row[5] == AllSourceList[SourceNum] and SearchTag in str(row):
                print(f'{LineCounter} ::: {row}')
                LineCounter += 1

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

        print('Вывести список технологий - 1')
        print('Вывести список доменов - 2')
        print('Вывести список функций - 3')
        print('Вывести список атрибутов - 4')
        print('Вывести список ученых - 5')
        print('Вывести список источников - 6')
        print('Вывести список связанных технологий - 7')
        print('Выгрузить результаты в текстовый файл - 8')
        print('Вернуться в главное меню - 0')

        SearchCounter = int(input('Введите номер пункта: '))

        if SearchCounter == 1:
            print('Технологии:')
            for i in range(0, len(SearchTechnologyList)):
                print(f'{i} ::: {SearchTechnologyList[i]}')
        elif SearchCounter == 2:
            print('Домены:')
            for i in range(0, len(SearchDomainList)):
                print(f'{i} ::: {SearchDomainList[i]}')
        elif SearchCounter == 3:
            print('Функции:')
            for i in range(0, len(SearchFuncList)):
                print(f'{i} ::: {SearchFuncList[i]}')
        elif SearchCounter == 4:
            print('Атрибуты:')
            for i in range(0, len(SearchAtributeList)):
                print(f'{i} ::: {SearchAtributeList[i]}')
        elif SearchCounter == 5:
            print('Ученые:')
            for i in range(0, len(SearchScientistList)):
                print(f'{i} ::: {SearchScientistList[i]}')
        elif SearchCounter == 6:
            print('Источники:')
            for i in range(0, len(SearchSourceList)):
                print(f'{i} ::: {SearchSourceList[i]}')
        elif SearchCounter == 7:
            print('Связанные технологии:')
            for i in range(0, len(SearchConnectTechnologiesList)):
                print(f'{i} ::: {SearchConnectTechnologiesList[i]}')
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
    print(Fore.LIGHTRED_EX)
    print('*** Поиск совпадений по базе данных ***')
    while True:
        print(Fore.LIGHTBLUE_EX)
        print('Поиск совпадений по всем источникам - 1')
        print('Поиск совпадений по конкретному источнику - 2')
        print('Вернуться в главное меню - 0')

        print(Fore.LIGHTGREEN_EX)
        SearchCounter = int(input('Введите номер пункта: '))

        if SearchCounter == 1:
            SearchAllDatabase()
        elif SearchCounter == 2:
            SearchBySource()
        elif SearchCounter == 0:
            break
        else:
            print(Fore.LIGHTRED_EX)
            print('*** Пожалуйста, проверьте корректность ввода ***')

#Показать содержимое базы данных
def ShowDatabase():
    print(Fore.LIGHTRED_EX)
    print('*** Просмотр содержимого базы данных ***')
    while True:
        print(Fore.LIGHTBLUE_EX)
        print('Просмотр всех технологий - 1')
        print('Просмотр технологий по источнику - 2')
        print('Вернуться в главное меню - 0')

        print(Fore.LIGHTGREEN_EX)
        ShowCounter = int(input('Введите номер пункта: '))

        if ShowCounter == 1:
            ShowAllDatabase()
        elif ShowCounter == 2:
            ShowDatabaseBySource()
        elif ShowCounter == 0:
            break
        else:
            print(Fore.LIGHTRED_EX)
            print('*** Пожалуйста, проверьте корректность ввода ***')

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
    print(Fore.LIGHTRED_EX, '*** Start work ***')

    while True:
        print(Fore.LIGHTRED_EX)
        print('*** Программа НИО МАИ 317 по поиску технологий ***')
        print(Fore.LIGHTBLUE_EX)
        print('Найти совпадения по базе данных - 1')
        print('Добавить новую запись в базу данных - 2')
        print('Показать содержимое базы данных - 3')
        print('Внести изменения в существующую строку базы данных - 4')
        print('ВЫЙТИ ИЗ ПРОГРАММЫ - 0')

        print(Fore.LIGHTGREEN_EX)
        FirstCounter = int(input('Введите номер пункта: '))

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

"""
task_02.py

Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры
в свойства. Задачи должны решаться через вызов методов экземпляра.
"""
import os
from pathlib import Path
from serialization import base_serialization as bs


def show_comparison(message_: str, result_: bool):
    if result_:
        print(f"{message_} equal.")
    else:
        print(f"{message_} not equal.")


if __name__ == '__main__':
    # получаем текущий рабочий каталог
    work_path = os.getcwd()

    ps = bs.Serialization()
    # рекурсивно обходим директорию и сохраняем результат в переменной
    res_list = ps.dir2list(work_path)

    # сохраняем переменную в файлах формата json, csv, pickle
    ps.save2json(res_list, Path('file_in.json'))
    ps.save2csv(res_list, Path('file_in.csv'))
    ps.save2pickle(res_list, Path('file_in.pickle'))

    # загружаем поочерёдно содержимое файлов в тестовую
    # переменную res_ и сравниваем её с исходной переменной res_list
    pickle_list = ps.load4pickle(Path('file_in.pickle'))
    res_ = ps.list_comparison(pickle_list, res_list)
    show_comparison("Lists res_list and pickle_list are", res_)

    csv_list = ps.load4csv(Path('file_in.csv'))
    res_ = ps.list_comparison(csv_list, res_list)
    show_comparison("Lists res_list and csv_list are", res_)

    json_list = ps.load4json(Path('file_in.json'))
    res_ = ps.list_comparison(json_list, res_list)
    show_comparison("Lists res_list and json_list are", res_)
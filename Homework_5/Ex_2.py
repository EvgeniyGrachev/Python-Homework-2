# Задание 2. 
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

print(parse_path("F:Data Engineer\Погружение в Python\Ex_2.py"))
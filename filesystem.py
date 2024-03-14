# Работа с файлами

import os

# информация о текущем файле
print(
    os.getcwd()
)
# result:
# d:/Web/412/tspu-group-412-main/filesystem.py

# Получить список файлов в директории
print(
    os.listdir()
)

# проверка есть ли директория
print(
    os.path.isdir('homeworks')
)

for f in os.listdir():
    print(
        f'is dir: {f}: ', os.path.isdir(f)
    )

# result:
# is dir: arr.py False
# is dir: dict_01.py False
# is dir: filesystem.py False
# is dir: hello_word.txt False
# is dir: homeworks True
# is dir: homework_1.txt False
# is dir: homework_2.txt False
# is dir: homework_3.txt False
# is dir: main.py False
# is dir: README.md False
# is dir: str.py False

# создание директорий
    
# os.mkdir('home_01/work_1')
# if not os.path.isdir('home_01/work_1'):
    # os.makedirs('home_01/work_1')

# def make_dirs(path):
#     if not os.path.isdir(path):
#         os.makedirs(path)

# make_dirs('home_01/work_2')




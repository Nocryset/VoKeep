from database.Core import engine as connect
from sqlalchemy import select, insert
from database.tables import users, words, languages, translations, vocabulary
from os import path

class User():
    def __init__(self, name, password):
        self.user_name = name
        self.user_password = password
        print("Welcome, {}".format(self.user_name))


current_user = None


def find_word():
    ...
# ToDo Поиск наличия слова в словаре что есть родным для языка
# ToDo Создание таблицы словарей для каждого языка
# ToDo создать таблицу со статистикой: Слово проверялось последний раз, слово переведно верно N раз, всего попыиток
#  Правила: Слово считаеться выученым если
#  слово введено верно И количесво попыток ровно верным ответам И
#  количество ошибок с множетелем соответстует максимальному значению для даного количества ошибок


def show_coeficient():
    for n in range(100):
        print("Если сделано ошибок {2} то для того чтобы выучить слово нужно угадать раз {1} из {0} попыток "
              .format(3*(n + 1) + n, 3*(n + 1), n))


def registration():
    print("Enter user name: ")
    name = input()

    print("Enter password: ")
    password = input()

    ins = users.insert()
    connect.execute(ins, name=name, password=password)
    print("Registration complete! Please login again!")


def upload_from_file():
    file_path = path.abspath("voc.txt")
    if path.exists(file_path):
        f = open(file_path)
    else:
        f = open(file_path, "w+")
        print("File not found! Create new file!")
    if len(f.read()):
        print("File full")
    else:
        print("File empty")


def upload_one():
    print("enter words with pattern: word1, lang1, word2, lang2")
    data = input()
    data.split(", ")
    tr = translations.insert()
    w = words.insert()
    la = languages.insert()
    voc = vocabulary.insert()
    connect.execute()


if __name__ == '__main__':
    while not current_user:
        print("Enter user name: ")
        name = input()

        print("Enter password: ")
        password = input()

        print('Searching in database')

        s = select([users]).where(users.c.name == name).where(users.c.password == password)
        result = connect.execute(s, name=name, password=password)

        if result.rowcount:
            row = result.fetchone()
            current_user = User(row[1], row[2])
            result.close()
        else:
            print("Not user. Do you want to registration. Or try again")
            command = input("Input 'R' to reg or skip if you try again, or 'exit' to close")
            if command.upper() == "R":
                registration()
            elif command.upper == "EXIT":
                exit()
            else:
                current_user = None
    upload_from_file()
    upload_one()
    # ToDo load woeds
    #  from file

    ...




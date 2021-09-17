"""
Домашнее задание №2

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(str1, str2):
    if type(str1) == str and type(str2) == str:
        if len(str1) == len(str2):
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
    return 0
if __name__ == "__main__":
    print(main('hi', 'hello'))
    print(main(123, 'hello'))
    print(main('hello', 'hello'))
    print(main('hello', 'cat'))
    print(main('hi', 'learn'))

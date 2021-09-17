"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_grades = [
   {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
   {'school_class': '5b', 'scores': [5, 2, 3, 4, 3]},
   {'school_class': '6c', 'scores': [2, 5, 3, 4, 5]},
   {'school_class': '9a', 'scores': [5, 3, 5, 5, 4]},
]
def main():
    school_average = []
    for name in school_grades:
        all_names = name.get('school_class')
        all_marks = name.get('scores')
        res = sum(all_marks) / len(all_marks)
        print(f'Средний балл по классу  "{all_names}": ', res)
        school_average.append(res)
    print(f'Средний балл по школы : {round(sum(school_average) / len(school_average),2)}')
if __name__ == "__main__":
    main()




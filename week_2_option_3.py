"""
Написать функцию ask_user(), чтобы с помощью input() спрашивать пользователя
"Как дела ?", пока он не ответит "Хорошо"
"""
def ask_user():
    while True:
        user_input = input('Как дела ? ')
        if user_input == 'Хорошо':
            print('Пока !')
            break

if __name__=='__main__':
    ask_user()

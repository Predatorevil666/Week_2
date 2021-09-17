"""
При помощи функции get_answer() отвечать на вопросы пользователя в
ask_user(), пока он не скажет "Пока !"
"""
answers = {'Привет': 'Привет !',
           'Как твои дела ?': 'Нормально',
           'Что делаешь ? ':'Программирую'}

def get_answer(question):
    return answers.get(question)
def ask_user_2():
    while True:
        user_input = input('Поговори со мной : ').capitalize()
        if user_input == 'Пока !'.capitalize():
            print('Пока !')
            break
        else:
            print(get_answer(user_input))
if __name__=='__main__':
    ask_user_2()

"""Приложение для обучения английскому. Программа по очереди задает вопросы и предлагает
вписать пропущенное слово"""

# Вводные данные
questions = ['My name *** Vova', 'I *** a coder', 'I live *** Moscow']
answers = ['is', 'am', 'in']
printing = ['First question', 'Second question', 'Third question']
correct_answers = 0
scores = 9

# Сперва программа здоровается и предлагает начать.
print('Привет! Предлагаю проверить свои знания английского!')
print('Наберите "ready", чтобы начать!')

user_input = input('* ')

# Если пользователь не набрал "ready" — программа завершается.
if user_input != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль.')
    print('Сайонара!')
    exit()

# Если пользователь набрал "ready" – программа начинает задавать вопросы:
else:
    print('Молодец! Давай скорее начнем!')

# Программа задает вопросы

for question, answer, print_ in zip(questions, answers, printing):
    print(f'{print_}: {question}')
    attempts = 3
    while attempts != 0:
        if input('Ваш ответ: ') == answer:
            print('Ответ верный!')
            correct_answers += 1
            break
        else:
            attempts -= 1
            scores -= 1
            if attempts > 0:
                print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
            else:
                print(f'Увы, но нет. Верный ответ: {answer}')

# Подвод итогов
print("*" * 30)
print(f'\nВот и все! Вы ответили на {correct_answers} вопросов из {len(questions)} верно,'
      f'вы набрали {scores} баллов.')

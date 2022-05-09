"""Программа тест для инженера заправщика картриджей"""

# Необходимые переменные
correct_answers = 0
scores = 18
cartridges = ['Q2612A', '728', 'TK-1140', '3325', 'FAT-411', 'TN-1075']
brands = ['HP', 'CANON', 'KYOCERA', 'XEROX', 'PANASONIC', 'BROTHER']


# Сперва программа здоровается и предлагает начать
print('Привет! Тебе необходимо пройти тест. \nЕсли ты ответишь на все вопросы, ты получить работу')
print('Напиши свое имя и нажми Enter, чтобы начать')
user_name = input().upper()
# Описание задания
print(f'На экране будут появляться названия картриджей, тебе необходимо написать какая компания '
      f'выпускает это картридж')

# Первый вопрос
for index in range(len(cartridges)):
    attempts = 3
    while attempts != 0:
        print(f'Картридж {cartridges[index]}')
        user_input = input('Ваш ответ: ').upper()
        if user_input == brands[index]:
            if correct_answers == 5:
                print('Ответ верный')
                correct_answers += 1
                scores += 3
                break
            else:
                print('Ответ верный \n------------\nСледующий вопрос:')
                correct_answers += 1
                scores += 3
                break
        else:
            attempts -= 1
            print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
            scores -= 1

    else:
        print(f'Увы, но нет. Верный ответ: {brands[index]}\n{12 * "-"}')

# Подведение статистики
if scores >= 12:
    print(f'{12 * "-"}\nВот и все {user_name}! Вы ответили на {correct_answers} вопросов из'
          f' {len(cartridges)}'
          f' верно, вы набрали {scores} баллов.\nЭто значит вы прошли тест. Вы приняты на работу')
else:
    print(f'{12 * "-"}\nВот и все {user_name}! Вы ответили на {correct_answers} вопросов из'
          f' {len(cartridges)}'
          f' верно, вы набрали {scores} баллов.\nВы не прошли тест. Ты идешь работать дворником')



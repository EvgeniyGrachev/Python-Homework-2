# Задание 4. 
# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код: from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


import random

# число попыток угадать
attempt_number = 0

# получаем случайное число в диапазоне от 0 до 1000
number = random.randint(0, 1000)
print ('Сможешь угадать число от 0 до 1000?')

# пока пользователь не превысил число разрешенных попыток - 10
while attempt_number < 10:
   
    # получаем число от пользователя
    guess = int(input('Введите число: '))
    attempt_number += 1

    if guess < number:
        print ('Твое число меньше загаданного.')

    if guess > number:
        print ('Твое число больше загаданного.')

    if guess == number:
        break

if guess == number:
    print ('Число угадано, использовав {0} попыток!'.format(attempt_number))
else:
    print ('Не угадал! Загадано число {0}'.format(number))
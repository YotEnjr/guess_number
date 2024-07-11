from random import randint

zag = randint(1,100)
while True:
    ch_1 = int(input('Введите число: '))
    if ch_1 < zag:
        print('Ваше число меньше того, что загадано')
        
    if ch_1 > zag:
        print('Ваше число больше того, что загадано')
        
    if ch_1 == zag:
        print('Отличная интуиция! Вы угадали число :)')
        break
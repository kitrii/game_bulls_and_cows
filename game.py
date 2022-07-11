#Игра "Быки и коровы"
import random 
nesnumber = ''.join(random.sample('0123456789',4)) #генерируем 4-ёх значное число без повторений
cows = 0 
bulls = 0
while True:
    assumptionnumber = input('Введите четырёхзначное число: ')
    flag = False # устанавливаем flag для того, чтобы отловить ошибку с повторяющимися цифрами
    for i in assumptionnumber:
        if assumptionnumber.count(i) > 1:
            flag = True
    if flag == True:
        print('ОШИБКА! Цифры не должны повторяться.')
        continue
    if len(assumptionnumber) != 4: 
        print('ОШИБКА! Введите четырёхзначное число.')
        continue
    for i in range(4):
        if nesnumber[i] == assumptionnumber[i]:
            bulls += 1
    if bulls == 4:
        print()
        print('Вы угадали загаданное число!')
        print('Поздравляем!')
        break
    print(f'bulls = {bulls}')
    bulls = 0
    for i in nesnumber:
        if i in assumptionnumber and nesnumber.index(i) != assumptionnumber.index(i):
            cows += 1
    print(f'cows = {cows}')
    cows = 0
    print('Продолжайте отгадывать.')
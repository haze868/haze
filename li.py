from random import randint
from time import sleep
from mine import*
from pi import*
def fight(player,enemy):
    round = randint(1, 2)
    enemy1 = enemies[enemy]
    enemy1_hp = enemies[enemy]['hp']
    print('Враг', enemy['name'])
    print(enemy['script'])
    name = input('Нажми "ДА" чтобы продолжить')
    
    while player['hp'] > 0 or enemy['hp'] > 0:
        player['hp'] - ['attack']
        print(player['hp'])
        sleep(1)
        enemy['hp'] - player['attack']
        print(enemy['hp'])
        sleep(1)
    if player('hp') < 0:
        print('Враг:', {enemy['name']})
        print('Ты проиграл')
    else:
        print('Враг:', {enemy['name']})
        print('Ты выиграл')
    player['hp'] = 100
    return enemy
def training(trainingtype):
    for i in range(0,100,20):
        print('Тренировка завершена на {i}%')
        sleep(2)
    if trainingtype == '1':
        player['attack'] += 4
        print('Тренировка окончена.Ваша атака равна:', {player['attack']})
    elif trainingtype == 4:
        player['armor'] -= .9
        print('Тренировка окончена.Ваша броня:', {100 - player['armor'] * 100})
              
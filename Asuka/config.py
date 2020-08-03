import time
print("Hello user, welcome to config screen.")
time.sleep(0.6)
print("Please choose a game mode.")
time.sleep(0.5)
while True:
    gameMode = input('Choose from; easy, normal, hard, lunatic: ')
    if gameMode == 'easy':
        print('Noob')
        enemyAmount = 50
        Life = 5
        enemyMaxSpeed = 2
        
    elif gameMode == 'normal':
        print('Mediocre')
        enemyAmount = int(100)
        Life = int(5)
        enemyMaxSpeed = int(4)

    elif gameMode == 'hard':
        print('Epic')
        enemyAmount = 150
        Life = 3
        enemyMaxSpeed = 6

    elif gameMode == 'lunatic':
        print('Overconfident')
        enemyAmount = 200
        Life = 1
        enemyMaxSpeed = 8

    break
enemyAmount = int(enemyAmount)
Life = int(Life)
enemyMaxSpeed = int(enemyMaxSpeed)
initLife = int(Life)
